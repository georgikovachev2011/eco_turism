from django.shortcuts import render
from django.http import HttpResponse
from signup.models import Signup
from rest_framework.decorators import api_view
from . serializers import SignupSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers

@swagger_auto_schema(
        method="post",
        request_body=SignupSerializer
)
@api_view(["POST"])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid()

    if serializer.data['password1'] != serializer.data['password2']:
        raise serializers.ValidationError({
                "password": "Passwords do not match."
            })
        return
    
    signup = Signup(username = serializer.data['username'],
                    email = serializer.data['email'],
                    password = serializer.data['password1'],
                        )
    signup.save()
    return HttpResponse()