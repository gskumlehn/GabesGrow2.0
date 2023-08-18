from django.shortcuts import render
from apps.config.models import GrowConfig, GrowConfigHistory

def index(request):
    config = GrowConfig.objects.filter(id=1)
    history = GrowConfigHistory.objects.orderBy("date").values()
    return render(request, 'config/show.html', {"config": config, "history": history})
