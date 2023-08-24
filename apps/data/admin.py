from django.contrib import admin
from apps.data.models import AirData
class ListAirData(admin.ModelAdmin):
    list_display = ('id', 'date', 'temperature', 'humidity')
    list_display_links = ('id', 'date', 'temperature', 'humidity')
    list_per_page = 30

admin.site.register(AirData, ListAirData)