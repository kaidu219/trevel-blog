from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Tours, Country
from django.core.paginator import Paginator
from django.views import View
from django.db.models import Q
from datetime import datetime, date
# Create your views here.

class ToursView(TemplateView):
    template_name = 'destination.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tours = Tours.objects.all()
        paginator = Paginator(tours, 3)
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
        print(context)

        tour = Tours.objects.get(pk=kwargs.get('id'))
        countries = Country.objects.all()
        context['tour'] = tour
        context['countries'] = countries
        
        return context


class CountryTourView(DetailView):
    model = Country
    context_object_name = 'country'
    template_name = 'country.html'
    pk_url_kwarg = 'slug'

class SearchView(View):

    
    def get(self, request):
        tours = Tours.objects.order_by()
        keyword = request.GET.get('keyword')
        startdate = request.GET.get('startdate')
        enddate = request.GET.get('enddate')
        price = request.GET.get('price')

        if keyword:
            tours = tours.filter(Q(tour_name__icontains=keyword) | Q(description__icontains=keyword))
                

        if len(startdate) >10 or len(enddate)>10:
            startdate = startdate.split('/')
            enddate = enddate.split('/')
            startdate = [int(i) for i in startdate if i.isdigit()]
            startdate = [startdate[-1], startdate[0], startdate[1]]
            enddate = [int(i) for i in enddate if i.isdigit()]
            enddate = [enddate[-1], enddate[0], enddate[1]]
            
            startdate = date(*startdate)
            enddate = date(*enddate)

            
            tours = tours.filter(Q(start_date__gte=startdate) | Q(start_date__lte=enddate))
            
        if price:
            print(price)
            tours = tours.filter(Q(price__lte=price))
            
        context = {
                'tours': tours,
            }
        return render(request, 'search.html', context)    
    