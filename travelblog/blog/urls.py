from django.contrib import admin
from django.urls import path, re_path
from .views import BlogView

urlpatterns = [
    path("/", BlogView.as_view(), name='blog'),
   
]