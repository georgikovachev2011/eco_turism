from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contaxts(request):
    return render(request, 'contaxts.html')

def email_sent(request):
    return render(request, 'email-sent.html')

def favorites(request):
    return render(request, 'favorites.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def pay(request):
    return render(request, 'pay.html')

def reset_password(request):
    return render(request, 'reset-password.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def signUpPage(request):
    return render(request, 'sign-up.html')


def signinPage(request):
    return render(request, 'sign-in.html')