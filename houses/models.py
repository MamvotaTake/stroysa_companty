from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class House(models.Model):
    house_title = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    Novaya_settlement = models.CharField(blank=True, max_length=255)
    hall = models.CharField(blank=True, max_length=255)
    square_metres = models.CharField(max_length=255)
    floors = models.CharField(blank=True, max_length=100)
    bedroom = models.CharField(blank=True, max_length=100)
    bedroom_1 = models.CharField(blank=True, max_length=100)
    bedroom_2 = models.CharField(blank=True, max_length=100)
    bedroom_3 = models.CharField(blank=True, max_length=100)
    bedroom_4 = models.CharField(blank=True, max_length=100)
    nursery = models.CharField(blank=True, max_length=100)
    nursery_1 = models.CharField(blank=True, max_length=100)
    nursery_2 = models.CharField(blank=True, max_length=100)
    Kitchen = models.CharField(blank=True, max_length=100)
    living_room = models.CharField(blank=True, max_length=100)
    C_A = models.CharField(blank=True, max_length=100)
    boiler_room = models.CharField(blank=True, max_length=100)
    corridor = models.CharField(blank=True, max_length=100)
    garage = models.CharField(blank=True, max_length=100)
    Vestibule = models.CharField(blank=True, max_length=100)
    description = RichTextField()
    house_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    house_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    house_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    house_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    house_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    house_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_finished = models.BooleanField(default=False)
    is_not_finished = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.house_title
