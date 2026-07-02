from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PostForm
from .models import Post
from django.contrib.admin.views.decorators import staff_member_required
# ===========================
# HOME
# ===========================

def home(request):

    posts = Post.objects.filter(
        published=True
    ).order_by("-created_at")[:3]

    return render(request, "blog/home.html", {
        "posts": posts
    })


# ===========================
# JOURNAL
# ===========================

def journal(request):

    posts = Post.objects.filter(
        published=True
    ).order_by("-created_at")

    return render(request, "blog/journal.html", {
        "posts": posts
    })


# ===========================
# POST DETAIL
# ===========================

def post_detail(request, slug):

    post = get_object_or_404(
        Post,
        slug=slug,
        published=True
    )

    related_posts = Post.objects.filter(
        category=post.category,
        published=True
    ).exclude(id=post.id)[:3]

    return render(request,
                  "blog/post_detail.html",
                  {
                      "post": post,
                      "related_posts": related_posts
                  })


# ===========================
# ABOUT
# ===========================

def about(request):
    return render(request, "blog/about.html")


# ===========================
# CONTACT
# ===========================

def contact(request):
    return render(request, "blog/contact.html")


# ===========================
# LOGIN
# ===========================

def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("dashboard")

    return render(request, "blog/login.html")


# ===========================
# REGISTER
# ===========================

def register(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    return render(request,
                  "blog/register.html",
                  {
                      "form": form
                  })


# ===========================
# DASHBOARD
# ===========================
@staff_member_required
def dashboard(request):

    total_posts = Post.objects.count()

    posts = Post.objects.order_by("-created_at")[:5]

    return render(
        request,
        "blog/dashboard.html",
        {
            "total_posts": total_posts,
            "posts": posts
        }
    )

@staff_member_required
def new_post(request):

    form = PostForm()

    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect("my_posts")

    return render(
        request,
        "blog/new_post.html",
        {
            "form": form
        }
    )
@staff_member_required
def my_posts(request):

    posts = Post.objects.order_by("-created_at")

    return render(
        request,
        "blog/my_posts.html",
        {
            "posts": posts
        }
    )


@staff_member_required
def edit_post(request, pk):

    post = get_object_or_404(Post, pk=pk)

    form = PostForm(instance=post)

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect("my_posts")

    return render(
        request,
        "blog/new_post.html",
        {
            "form": form,
            "edit": True
        }
    )


@staff_member_required
def delete_post(request, pk):

    post = get_object_or_404(Post, pk=pk)

    post.delete()

    return redirect("my_posts")
# ===========================
# LOGOUT
# ===========================

def logout_user(request):

    logout(request)

    return redirect("home")