from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Команда"""
    list_display = ("id", "name", "lastname", "jobteam", "get_image")
    list_display_links = ("name",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"