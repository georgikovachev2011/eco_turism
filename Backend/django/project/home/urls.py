from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('contaxts/', views.contaxts, name="contaxts"),
    path('email_sent/', views.email_sent, name="email_sent"),
    path('favorites/', views.favorites, name="favorites"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('pay/', views.pay, name="pay"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('destination/', views.destination, name="destination"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('sign_in/', views.sign_in, name="sign_in"),
]