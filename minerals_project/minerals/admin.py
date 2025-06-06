from django.contrib import admin
from .models import Mineral

@admin.register(Mineral)
class MineralAdmin(admin.ModelAdmin):
    list_display = ('name', 'extraction_url', 'reserves_url')