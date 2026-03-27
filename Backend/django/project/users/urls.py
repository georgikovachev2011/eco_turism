from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('resetpass/', views.resetpass, name = "resetpass"),
    path('sign-in/', views.signinPage, name="signin"),
    path('sign-up/', views.signUpPage, name="signup"),
]