from django.shortcuts import render
from django.http import HttpResponse
from .models import View_All_destinations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ViewAllDestinationsSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method="get", responses={200: ViewAllDestinationsSerializer(many=True)})
@api_view(["GET"])
def view_dest(request):
    destinations = View_All_destinations.objects.all()
    serializer = ViewAllDestinationsSerializer(destinations, many=True)
    return Response(serializer.data)