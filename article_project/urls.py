from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("articles.urls")),

    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]