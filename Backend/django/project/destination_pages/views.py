from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination_Pages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ListDestinationsPagesSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method="get", responses={200: ListDestinationsPagesSerializer(many=True)})
@api_view(["GET"])
def dest_pages(request):
    destinations = Destination_Pages.objects.all()
    serializer = ListDestinationsPagesSerializer(destinations, many=True)
    return Response(serializer.data)


