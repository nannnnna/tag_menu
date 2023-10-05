from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from core.models import MenuItem


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'position']
