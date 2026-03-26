from django.shortcuts import render
from django.http import HttpResponse
from models import Booking

def book(request):
    #add validations
    booking = Booking(name = request.name,
                      email = request.email,
                      phone_num = request.phone_num,
                      date_start = request.date_start,
                      date_end = request.date_end,
                      hotel_id = request.hotel_id )
    booking.save()
    return HttpResponse()

