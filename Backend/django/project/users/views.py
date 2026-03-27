from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from users.models import Userdata
from rest_framework.decorators import api_view
from . serializers import SignupSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from . serializers import SigninSerializer
import smtplib
from email.mime.text import MIMEText
import random
from . serializers import ResetpasswordSerializer
from . serializers import Codeconfirm


@swagger_auto_schema(
        method="post",
        request_body=SignupSerializer
)
@api_view(["POST"])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid()
    if Userdata.objects.filter(username=username).exists():
        raise serializers.ValidationError({
            "username": "A user with this username already exists."
        })
    if serializer.data['password1'] != serializer.data['password2']:
        raise serializers.ValidationError({
                "password": "Passwords do not match."
            })
        return
    
    users = Userdata(username = serializer.data['username'],
                    email = serializer.data['email'],
                    password = serializer.data['password1'],
                        )
    users.save()
    return HttpResponse()

@swagger_auto_schema(
        method="post",
        request_body=SigninSerializer
)
@api_view(["POST"])
def signin(request):
    serializer = SigninSerializer(data=request.data)
    serializer.is_valid()
    try:
        user = Userdata.objects.get(username=serializer.validated_data['username'])
    except Userdata.DoesNotExist:
        raise serializers.ValidationError({
            "detail": "Invalid username or password"  


        })
    
    if serializer.data['password'] != user.password:
        raise serializers.ValidationError({
            "password_or_username_wrong": "Password or username doesnt match"
        })
        return
    else:
        return HttpResponse()

@swagger_auto_schema(
        method="post",
        request_body=ResetpasswordSerializer
)
@api_view(["POST"])
def resetpass(request):
    rand0m = random.randint(0, 99999)
    Onetimecode = f"{rand0m:05d}"
    serializer = ResetpasswordSerializer(data=request.data)
    serializer.is_valid()
    user = Userdata.objects.get(email=serializer.validated_data['email'])
    if not user:
        return HttpResponse("User not found", status=404)
    user.code = Onetimecode
    user.save()
    msg = MIMEText(f"Your one time use code is {Onetimecode}")
    msg["Subject"] = "Reset_email"
    msg["From"] = "djangodjangiev@gmail.com"
    msg["To"] = serializer.data["email"]
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("djangodjangiev@gmail.com", "uadm szfc qyaa ymsi")
        server.send_message(msg)
    
    return HttpResponse()

def Codeconfirm(request):
     serializer = Codeconfirm(data=request.data)
     serializer.is_valid()
     try:
         user = Userdata.objects.get(code=serializer.data['code'])
         user.password = serializer.data['password']
         user.save()
     except Userdata.DoesNotExist:
        raise serializers.ValidationError({
            "detail": "Invalid code"  
        })
     return HttpResponse()
     