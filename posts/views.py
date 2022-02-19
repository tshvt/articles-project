from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePostForm, EditPostForm
from django.contrib.auth.decorators import login_required
from .decorators import user_is_author, is_author, is_public


def index(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, "posts/index.html", {"posts": posts})


@is_public
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post.html", {"post": post})


@login_required(login_url="login")
@is_author(login_url="login")
def new_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    else:
        form = CreatePostForm()
    return render(request, "posts/new-post.html", {"form": form})


@login_required(login_url="login")
@user_is_author
def edit_post(request, slug):
    post_to_update = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post_to_update)
        if form.is_valid():
            form.save()
            post = Post.objects.get(title=form.cleaned_data['title'])
            return redirect("post-details", slug=post.slug)
    form = EditPostForm(instance=post_to_update)
    return render(request, "posts/edit-post.html", {"form": form, "post": post_to_update})


@login_required(login_url="login")
@user_is_author
def delete_post(request, slug):
    post_to_delete = Post.objects.get(slug=slug)
    post_to_delete.delete()
    return redirect('home-page')
