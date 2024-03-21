from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from .models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def add_product(request):
    if request.method == "GET":
        form = forms.ProductForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Added.")
    else:
        form = forms.ProductForm()
    return render(request, "productform.html", {
        "form": form
    })


@login_required(login_url='login')
def update_product(request, p_id):
    product = Product.objects.get(pk=p_id)
    if request.method == "GET":
        form = forms.ProductForm(request.GET or None, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Updated.")
    else:
        form = forms.ProductForm(instance=product)
    return render(request, "productform.html",{
        "form": form
    })


@login_required(login_url='login')
def delete_proucts(request, p_id):
    Product.objects.get(pk=p_id).delete()
    return HttpResponse("Product Deleted.")
