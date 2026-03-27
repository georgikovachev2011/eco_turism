from django.shortcuts import render
from django.http import HttpResponse
from signup.models import Signup
from rest_framework.decorators import api_view
from . serializers import SignupSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
        method="post",
        request_body=SignupSerializer
)
@api_view(["POST"])
def book(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid()
    #add validations
    signup = Signup(name = serializer.data['name'],
                      email = serializer.data['email'],
                      phone_num = serializer.data['phone_num'],
                      date_start = serializer.data['date_start'],
                      date_end = serializer.data['date_start'],
                      hotel_num = serializer.data['hotel_num'] )
    signup.save()
    return HttpResponse()