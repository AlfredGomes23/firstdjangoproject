from django.shortcuts import render


# Create your views here.
def dlogin(request):
    return render(request, "DLogin.html")


def dsignup(request):
    pass
