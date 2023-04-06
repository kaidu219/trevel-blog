from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tours, Country
from django.core.paginator import Paginator

# Create your views here.

class ToursView(TemplateView):
    template_name = 'destination.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tours = Tours.objects.all()
        paginator = Paginator(tours, 2)
        page = self.request.GET.get('page')
        paged_tours = paginator.get_page(page)
        countries = Country.objects.all()
        context['tours'] = tours
        context['countries'] = countries
        context['paged_tours'] = paged_tours
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
