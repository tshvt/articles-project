from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, MyUserCreationForm


def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home-page")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect("home-page")


def register_user(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("home-page")
    else:
        form = MyUserCreationForm()
    return render(request, 'users/register.html', {"form": form})

