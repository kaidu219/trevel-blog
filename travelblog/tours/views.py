from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tours, Country


# Create your views here.

class ToursView(TemplateView):
    template_name = 'destination.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tours = Tours.objects.all()
        context['tours'] = tours
        return context
    
class ToursDetailView(TemplateView):
    model = Tours
    context_object_name = 'tour'
    template_name = 'tour-single.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tour = Tours.objects.get(pk=kwargs.get('id'))
        countries = Country.objects.all()
        context['tour'] = tour
        context['countries'] = countries
        return context
