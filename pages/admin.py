from django.contrib import admin
from django.utils.html import format_html

from pages.models import Testimonial


# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:30%;">'.format(object.photo.url))

    thumbnail.short_description = 'Person Photo'
    list_display = ('thumbnail', 'first_name', 'created_date',)
    list_display_links = ('thumbnail', 'first_name',)


admin.site.register(Testimonial, TestimonialAdmin)
