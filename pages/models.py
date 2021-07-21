from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Testimonial(models.Model):
    first_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
