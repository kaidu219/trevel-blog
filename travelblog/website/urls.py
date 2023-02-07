from django.contrib import admin
from django.urls import path, re_path
from .views import index, contact_us, about_us

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact_us, name='contact' ),
    path('about/', about_us, name='about'),
]