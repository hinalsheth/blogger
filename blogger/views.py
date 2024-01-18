from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .models import BlogPost
from .forms import BlogPostForm, UserRegisterForm


def home(request):
    return post_list(request)


def post_list(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "blogger/post_list.html", {"posts": posts})


@login_required
def submit_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")  # Redirect to the list of blog posts
    else:
        form = BlogPostForm()
    return render(request, "blogger/submit_post.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": form})
