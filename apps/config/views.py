from apps.config.forms import ConfigForm
from apps.config.models import GrowConfig, GrowConfigHistory
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request, config_id):
    config = GrowConfig.objects.get(id=config_id)
    form = ConfigForm(instance=config)
    history = GrowConfigHistory.objects.filter(id=config_id).order_by("date").values()
    return render(request, 'config/show.html', {"config": config, "history": history, "form": form})

def edit(request, config_id):
    config = GrowConfig.objects.get(id=config_id)
    form = ConfigForm(request.POST, instance=config)

    if form.is_valid():
        form.save()
        messages.success(request, "Config updated")
    else:
        messages.error(request, "Config update failed")

    return redirect('index', {"config_id": config_id})

