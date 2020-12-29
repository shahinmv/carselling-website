from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40" style="border-radius: 10px;"/>'.format(object.car_photo1.url))

    thumbnail.short_description = 'Car Photo'
    list_display = ('id', 'thumbnail', 'city','car_title', 'car_model','year','body_style','fuel', 'price', 'is_featured',)
    list_display_links = ('id','thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title','car_model', 'city',  'fuel')
    list_filter = ('city', 'car_title', 'body_style', 'fuel',)


admin.site.register(Car, CarAdmin)

