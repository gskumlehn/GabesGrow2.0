from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from apps.config.models import GrowConfig, GrowConfigHistory

def index(request):
    config = GrowConfig.objects.filter(id=1)
    lastUpdate = parse_datetime(config.lastUpdate).strftime("%d/%m/%Y - %H:%M")
    history = GrowConfigHistory.objects.order_by("date").values()
    return render(request, 'config/show.html', {"config": config, "lastUpdate": lastUpdate, "history": history})
