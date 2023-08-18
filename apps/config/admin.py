from django.contrib import admin
from apps.config.models import GrowConfig, GrowConfigHistory
class ListGrowConfig(admin.ModelAdmin):
    list_display = ('id', 'stageType', 'watering', 'lastUpdate')
    list_display_links = ('id', 'lastUpdate')
    list_editable = ('stageType', 'watering')
    list_per_page = 1

class ListGrowConfigHistory(admin.ModelAdmin):
    list_display = ('description', 'date')
    list_per_page = 10

admin.site.register(GrowConfig, ListGrowConfig)
admin.site.register(GrowConfigHistory, ListGrowConfigHistory)
