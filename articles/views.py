from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Article


# ---------------- HOME ----------------
def index(request):
    articles = Article.objects.all()
    return render(request, "articles/index.html", {"articles": articles})


# ---------------- DETAIL ----------------
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "articles/detail.html", {"article": article})


# ---------------- CREATE (NEW) ----------------
@login_required
def create_article(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        Article.objects.create(title=title, content=content)
        return redirect("index")

    return render(request, "articles/create.html")


# ---------------- SIGN UP ----------------
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "articles/signup.html", {"error": "User exists"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("index")

    return render(request, "articles/signup.html")


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "articles/login.html", {"error": "Invalid login"})

    return render(request, "articles/login.html")


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect("index")