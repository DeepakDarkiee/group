from django.shortcuts import render, redirect  
from django.http import HttpResponse,HttpResponseRedirect  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            user_name = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user=authenticate(username=user_name,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')
        else:
            messages.success(request,"incorrect username or password")
            return render(request,"account/login.html",{'form':fm})
    else:
        fm=AuthenticationForm()
    return render(request,"account/login.html",{'form':fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

