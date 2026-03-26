from django.shortcuts import render
from django.http import HttpResponse
from sign_up.models import Signup
from rest_framework.decorators import api_view
from .serializers import SignupSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
        method="post",
        request_body=SignupSerializer
)

@api_view(["POST"])
def sign_up(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid()
    Signup = Signup(name = serializer.data['name'],
                      username = serializer.data['email'],
                      email = serializer.data['phone_num'],
                      password = serializer.data['date_start'], )
    
    Signup.save()
    return HttpResponse()