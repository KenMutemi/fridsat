from registration.decorators import anonymous_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

@anonymous_required(home_url='/')
def login(request):
    return render(request, 'registration/login.html')

@anonymous_required(home_url='/')
def landing(request):
    return render(request, 'registration/landing.html')