from apps.config.forms import ConfigForm
from apps.config.models import GrowConfig
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request, config_id):
    config = GrowConfig.objects.get(id=config_id)
    form = ConfigForm(instance=config)
    return render(request, 'config/show.html', {"config": config, "form": form})

def edit(request, config_id):
    config = GrowConfig.objects.get(id=config_id)
    form = ConfigForm(request.POST, instance=config)

    if form.is_valid():
        updatedConfig = form.save()
        if updatedConfig.lights:
            updatedConfig.lightOn
        else:
            updatedConfig.lightOff
        messages.success(request, "Config updated")
    else:
        messages.error(request, "Config update failed")

    return redirect('config', config_id=config_id)

