from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# ---------------- MEMORY STORAGE ----------------
ARTICLES = []
ID = 1


# ---------------- HOME ----------------
def index(request):
    return render(request, "articles/index.html", {
        "articles": ARTICLES,
        "user": request.user
    })


# ---------------- DETAIL ----------------
def detail(request, id):
    article = next((a for a in ARTICLES if a["id"] == id), None)
    return render(request, "articles/detail.html", {"article": article})


# ---------------- CREATE ----------------
@login_required
def create_article(request):
    global ID

    if request.method == "POST":
        ARTICLES.append({
            "id": ID,
            "title": request.POST["title"],
            "content": request.POST["content"]
        })
        ID += 1
        return redirect("index")

    return render(request, "articles/create.html")


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        
        print("Authenticated user:", user)  # Debugging statement
        if user:
            login(request, user)
            return redirect("index")

    return render(request, "articles/login.html")


# ---------------- SIGNUP ----------------
def signup(request):
    if request.method == "GET":
        return render(request, "articles/signup.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "articles/signup.html")

        user = User.objects.create_user(
            username=username,
            password=password
        )

        user.save()

        messages.success(request, "Account created successfully")
        return redirect("login")

# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect("index")