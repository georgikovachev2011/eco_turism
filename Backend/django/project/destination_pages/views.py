from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination_Pages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ListDestinationsPagesSerializer, DestinationPageSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method="post",
                             request_body=DestinationPageSerializer)
@api_view(["POST"])
def dest_pages(request):
    serializer = DestinationPageSerializer(data=request.data)
    serializer.is_valid()

    destinations = Destination_Pages.objects.get(id=serializer.data['id'])
    response = ListDestinationsPagesSerializer(destinations)
    return Response(response.data)
