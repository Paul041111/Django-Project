from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:id>/", views.detail, name="detail"),
    path("create/", views.create_article, name="create"),
]