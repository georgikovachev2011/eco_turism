from django.urls import path
from . import views

urlpatterns=[
    path('', views.view_dest, name="view_dest")
]