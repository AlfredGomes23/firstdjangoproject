from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, "home.html")


@login_required(login_url='login')
def newhome(request):
    return render(request, "newhome.html")


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {
        "products": products
    })
