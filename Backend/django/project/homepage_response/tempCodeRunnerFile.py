from django.shortcuts import render
from django.http import HttpResponse
from .models import List_destinations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ListDestinationsSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method="get", responses={200: ListDestinationsSerializer(many=True)})
@api_view(["GET"])
def home_resp(request):
    destinations = List_destinations.objects.all()
    serializer = ListDestinationsSerializer(destinations, many=True)
    return Response(serializer.data)