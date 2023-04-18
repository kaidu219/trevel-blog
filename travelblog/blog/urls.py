from django.contrib import admin
from django.urls import path, re_path
from .views import BlogView, BlogDateilView, CategoryView

urlpatterns = [
    path("", BlogView.as_view(), name='blog'),
    path("<str:id>", BlogDateilView.as_view(), name='blog-detail'),
    path("<str:slug>/", CategoryView.as_view(), name='category'),
]