from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import Post
from django.contrib import messages


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "list",
        "obj_list": queryset,
    }
    return render(request, "posts/index.html", context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # Message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    print form.cleaned_data.get("title")
    return render(request, "posts/post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Detail",
        "object": instance,
    }
    return render(request, "posts/detail.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Detail",
        "object": instance,
        "form": form,
    }
    return render(request, "posts/post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")
