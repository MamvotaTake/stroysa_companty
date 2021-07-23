from datetime import datetime

from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    house_id = models.IntegerField()
    customer_need = models.CharField(max_length=255)
    house_title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(blank=True, max_length=255)
    phone = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
