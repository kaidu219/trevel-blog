from django.shortcuts import render
from .models import Feedback
from blog.models import Blog
from tours.models import Tours, Country
from .forms import ContactForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.contrib import messages


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            message_mail = f'Your have massage in CarSelling Platform from {name} regarding: subject: {subject} message: {message} \n\n\Sender Details: Email: {email} '
            
            admin_info = User.objects.get(is_superuser=True)
            admin_email = 'carsellplatformdjango@gmail.com'

            send_mail(
                subject,
                mark_safe(message_mail),
                email,
                ['carsellplatformdjango@gmail.com', admin_email],
                fail_silently=False,
            )
            send_mail(
                'Vacation',
                'Ваше обращение было отправлено, скоро дадим ответ',
                admin_email,
                [email],
                 fail_silently=False,
            )
            # messages.success(request, 'Your message has been successfully send!')
    else:
        form = ContactForm()


    context = {
            'form': form,
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