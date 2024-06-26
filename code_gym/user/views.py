from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import signup_form, login_form


def index(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1> yes</h1>")
    return HttpResponse("<h1> no</h1>")


def signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signup_form()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('index')
    else:
        form = login_form()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')
