from django.shortcuts import render, get_object_or_404

# Create your views here.
from houses.models import House


def houses(request):
    houses = House.objects.order_by('-created_date')
    finished_houses = House.objects.order_by('-created_date').filter(is_finished=True)
    houses_not_finished = House.objects.order_by('-created_date').filter(is_not_finished=True)

    data = {
        'houses': houses,
        'finished_houses': finished_houses,
        'houses_not_finished': houses_not_finished,
    }
    return render(request, 'houses/house.html', data)


def house_detail(request, id):
    single_house = get_object_or_404(House, pk=id)

    data = {
        'single_house': single_house,
    }

    return render(request, 'houses/house_detail.html', data)
