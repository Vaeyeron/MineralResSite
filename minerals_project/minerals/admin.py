from django.contrib import admin
from .models import Mineral

@admin.register(Mineral)
class MineralAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'extraction_url', 'reserves_url')