from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def dlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful.")
            return redirect("home")
        else:
            messages.success(request, "There was an error occurred.")
            return redirect("dlogin")
    return render(request, "DLogin.html")


def dsignup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        if request.POST["password1"] == request.POST["password2"]:
            password = request.POST["password1"]
            print(username, email, password)
            try:
                new_user = User.objects.create_user(username, email, password)
                new_user.save()
                messages.success(request, "SignUp Successful.")
                return redirect("login", )
            except:
                messages.success(request, "User name exist.")
        else:
            messages.success(request, "Password didn't matched.")
    return render(request, "DLogin.html")
