from django.contrib import admin
from apps.config.models import GrowConfig
class ListGrowConfig(admin.ModelAdmin):
    list_display = ('id', 'date', 'temperature', 'humidity')
    list_display_links =  ('id', 'date', 'temperature', 'humidity')
    list_per_page = 30

admin.site.register(GrowConfig, ListGrowConfig)
