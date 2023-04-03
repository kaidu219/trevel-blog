from django.shortcuts import render
from .models import Feedback


from django.shortcuts import render, HttpResponse


def index(request):
    feedback = Feedback.objects.all()

    context = {
        'feedback': feedback,
    }

    return render(request, 'index.html', context)

def contact_us(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about.html')

def destination(request):
    return render(request, 'destination.html')