from django.shortcuts import render
from .models import Post
from . import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def posts(request):
    posts = Post.objects.all()
    return render(request, "Posts.html", {
        "posts": posts
    })


@login_required(login_url='login')
def add_post(request):
    if request.method == "GET":
        form = forms.PostForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse("Post Added.")
    else:
        form = forms.PostForm()
    return render(request, "PostForm.html", {"form": form})


@login_required(login_url='login')
def update_post(request, p_id):
    post = Post.objects.get(pk=p_id)
    if request.method == "GET":
        form = forms.PostForm(request.GET or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse("Post Updated.")
    else:
        form = forms.PostForm()
    return render(request, "PostForm.html", {"form": form})


@login_required(login_url='login')
def delete_post(request, p_id):
    Post.objects.get(pk=p_id).delete()
    return HttpResponse("Post Deleted.")
