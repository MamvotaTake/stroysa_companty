from datetime import datetime

from django.shortcuts import render

from houses.models import House
from pages.models import Testimonial


# Create your views here.
def home(request):
    testimonials = Testimonial.objects.all()
    houses = House.objects.order_by('-created_date')

    myDate = datetime.now()
    data = {
        'testimonials': testimonials,
        'myDate': myDate,
        'houses': houses,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    testimonials = Testimonial.objects.all()
    houses = House.objects.order_by('-created_date')
    myDate = datetime.now()

    data = {
        'testimonials': testimonials,
        'myDate': myDate,
        'houses': houses,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contacts(request):
    return render(request, 'pages/contacts.html')
