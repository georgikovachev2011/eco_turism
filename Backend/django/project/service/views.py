from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomerService
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
        method="post",
        request_body=CustomerSerializer
)
@api_view(["POST"])
def cust_serv(request):
    serializer = CustomerSerializer(data=request.data)
    serializer.is_valid()
    #add validations
    customer_service = CustomerService(name = serializer.data['name'],
                      email = serializer.data['email'],
                      subject = serializer.data['subject'],
                      message = serializer.data['message']
                      )
    customer_service.save()
    return HttpResponse()

