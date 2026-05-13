from django.shortcuts import render , redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import customregform
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth import logout
from django.shortcuts import redirect, render

def logout_view(request):
    if request.method == "POST":
        logout(request)    
    return redirect("Home")  # block GET

def logout_success(request):
    return render(request, "logout.html")

def register(request):
    if request.method == "POST":
        register_form = customregform(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"User created successfully")
            return redirect("Home")
    else:
        register_form = customregform()
    return render(request, "registration.html" ,{'register_form':register_form})
    # return HttpResponse("Registration form")
# 
