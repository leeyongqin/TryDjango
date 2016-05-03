from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post


def post_list(request):
    queryset = Post.objects.all()
    #instance = get_object_or_404(Post, id=2)
    context = {
        "obj_list": queryset,
    }
    return render(request, "posts/index.html", context)


def post_create(request):
    return HttpResponse('<h1>Create</h1>')


def post_detail(request, id=None):
    #queryset = Post.objects.get(id=id)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Detail",
        "object": instance,
    }
    return render(request, "posts/detail.html", context)


def post_update(request):
    return HttpResponse('<h1>Update</h1>')


def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')
