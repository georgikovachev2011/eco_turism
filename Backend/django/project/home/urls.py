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
    path('sign-in/', views.signinPage, name="signin"),
    path('sign-up/', views.signUpPage, name="signup"),
]