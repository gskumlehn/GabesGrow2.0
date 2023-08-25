from datetime import datetime
from django.shortcuts import render, redirect
from apps.data.functions import AirHumidityAndTemperature
from apps.data.models import AirData

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    humidity, temperature = AirHumidityAndTemperature.get()
    collectionTime = datetime.now().strftime("%H:%M")
    return render(request, 'dashboard/index.html',
                  {"humidity": humidity, "temperature": temperature, "time": collectionTime})

def data(request):
    data = AirData.objects.all()[0]
    return render(request, 'dashboard/data.html' ["data": data])

