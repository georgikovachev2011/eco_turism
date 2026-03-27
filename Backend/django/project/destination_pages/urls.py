from django.urls import path
from . import views

urlpatterns=[
    path('', views.dest_pages, name="dest_pages")
]