from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Booking
from rest_framework.decorators import api_view
from .serializers import BookingSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
        method="post",
        request_body=BookingSerializer
)
@api_view(["POST"])
def book(request):
    serializer = BookingSerializer(data=request.data)
    serializer.is_valid()
    #add validations
    booking = Booking(name = serializer.data['name'],
                      email = serializer.data['email'],
                      phone_num = serializer.data['phone_num'],
                      date_start = serializer.data['date_start'],
                      date_end = serializer.data['date_start'],
                      hotel_num = serializer.data['hotel_num'] )
    booking.save()
    return HttpResponse()

