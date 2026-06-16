from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:id>/", views.detail, name="detail"),
    path("create/", views.create_article, name="create_article"),
    path("edit/<int:id>/", views.edit_article, name="edit_article"),
    path("delete/<int:id>/", views.delete_article, name="delete_article"),

    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]