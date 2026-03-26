from django.urls import path
from . import views

urlpatterns = [
    path('', views.cust_serv, name="cust_serv")
]
