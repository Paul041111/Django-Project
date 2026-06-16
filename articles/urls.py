from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:id>/", views.detail, name="detail"),

    # ✅ THIS IS REQUIRED
    path("create/", views.create_article, name="create_article"),

    path("article/<int:id>/edit/", views.edit_article, name="edit_article"),
    path("article/<int:id>/delete/", views.delete_article, name="delete_article"),
]
