from django.contrib import admin
from django.urls import path, re_path
from .views import index, contact_us, about_us, destination

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact_us, name='contact' ),
    path('about/', about_us, name='about'),
    path('destination/', destination, name='destination'),
]