from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from apps.config.models import GrowConfig, GrowConfigHistory

def index(request):
    config = GrowConfig.objects.values()[0]
    history = GrowConfigHistory.objects.order_by("date").values()
    return render(request, 'config/show.html', {"config": config, "history": history})
