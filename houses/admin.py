from django.contrib import admin
from django.utils.html import format_html

from houses.models import House


# Register your models here.
class HouseAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:30%;">'.format(object.house_photo.url))

    thumbnail.short_description = 'House Photo'
    list_display = ('thumbnail', 'house_title', 'size', 'created_date', 'is_finished',)
    list_display_links = ('thumbnail', 'house_title',)


admin.site.register(House, HouseAdmin)
