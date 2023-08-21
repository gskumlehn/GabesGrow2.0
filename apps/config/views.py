from django.shortcuts import render
from apps.config.models import GrowConfig, GrowConfigHistory

def index(request, config_id):
    config = GrowConfig.objects.get(id=config_id)
    history = GrowConfigHistory.objects.order_by("date").values()
    return render(request, 'config/show.html', {"config": config, "history": history})
