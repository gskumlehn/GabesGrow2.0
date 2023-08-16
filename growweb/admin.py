from django.contrib import admin
from .models import GrowConfig, GrowConfigHistory, Stage

class ListGrowConfig(admin.ModelAdmin):
    list_display = ('id', 'stageType', 'watering', 'lastUpdate')
    list_display_links = ('id', 'lastUpdate')
    list_editable = ('stageType', 'watering')
    list_per_page = 1

class ListGrowConfigHistory(admin.ModelAdmin):
    list_display = ('description', 'date')
    list_per_page = 10

class ListStage(admin.ModelAdmin):
    list_display = ('type', 'lightOn', 'lightOff', 'phMin', 'phMax', 'tempMin', 'tempMax', 'soilHumMin', 'soilHumMax', 'airHumMin', 'airHumMax',)
    list_display_links = ('type', 'lightOn', 'lightOff', 'phMin', 'phMax', 'tempMin', 'tempMax', 'soilHumMin', 'soilHumMax', 'airHumMin', 'airHumMax',)
    list_per_page = 5

admin.site.register(GrowConfig, ListGrowConfig)
admin.site.register(GrowConfigHistory, ListGrowConfigHistory)
admin.site.register(Stage, ListStage)
