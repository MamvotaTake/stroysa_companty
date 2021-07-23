from django.shortcuts import render


# Create your views here.
from houses.models import House


def houses(request):
    houses = House.objects.order_by('-created_date')

    data = {
        'houses': houses
    }
    return render(request, 'houses/house.html', data)
