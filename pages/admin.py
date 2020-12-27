from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40" style = "border-radius: 10px"/>'.format(object.photo.url))
    
    thumbnail.short_description = 'Profile Photo'

    list_display = ('id','thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name',)

admin.site.register(Team, TeamAdmin)