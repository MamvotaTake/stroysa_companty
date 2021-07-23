from django.urls import path

from . import views

urlpatterns = [
    path('', views.houses, name='houses'),
    path('<int:id>', views.house_detail, name='house_detail'),

]
