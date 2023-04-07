from django.contrib import admin
from django.urls import path, re_path
from .views import ToursView, ToursDetailView, CountryTourView

urlpatterns = [
    path("", ToursView.as_view(), name='tours'),
    path("<str:id>", ToursDetailView.as_view(), name='tour-detail'),
    path("<str:slug>/", CountryTourView.as_view(), name='country'),
]