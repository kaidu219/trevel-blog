from django.shortcuts import render
from .models import Feedback
from blog.models import Blog
from tours.models import Tours, Country


from django.shortcuts import render, HttpResponse


def index(request):
    feedback = Feedback.objects.all()
    post = Blog.objects.all()[:3]
    tours = Tours.objects.all()[:6]
    countries = Country.objects.all()
    context = {
        'posts': post,
        'feedback': feedback,
        'tours': tours,
        'countries': countries,

    }

    return render(request, 'index.html', context)

def contact_us(request):
    post = Blog.objects.all()[:3]

    context = {
        'posts': post,
    }
    return render(request, 'contact.html', context)

def about_us(request):
    post = Blog.objects.all()[:3]
    feedback = Feedback.objects.all()
    context = {
        'posts': post,
        'feedback': feedback,
    }
    return render(request, 'about.html', context)

# def destination(request):
#     post = Blog.objects.all()[:3]
#     tours = Tours.objects.all()
#     context = {
#         'tours': tours,
#     }
#     return render(request, 'destination.html', context)