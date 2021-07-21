from datetime import datetime


from django.shortcuts import render

from pages.models import Testimonial


# Create your views here.
def home(request):
    testimonials = Testimonial.objects.all()

    myDate = datetime.now()
    data = {
        'testimonials': testimonials,
        'myDate': myDate

    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contacts(request):
    return render(request, 'pages/contacts.html')
