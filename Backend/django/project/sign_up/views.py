from django.shortcuts import render
from django.http import HttpResponse
from sign_up.models import Sign_up
from rest_framework.decorators import api_view
from .serializers import SignUpSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
        method="post",
        request_body=SignUpSerializer
)

@api_view(["POST"])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid()
    sign_up = Sign_up(name = serializer.data['name'],
                      username = serializer.data['username'],
                      email = serializer.data['email'],
                      password = serializer.data['password'], )
    
    sign_up.save()
    return HttpResponse()