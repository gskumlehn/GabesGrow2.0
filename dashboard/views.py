from datetime import datetime
from django.shortcuts import render
from data.functions import AirHumidityAndTemperature

def index(request):
    humidity, temperature = AirHumidityAndTemperature.get()
    collectionTime = datetime.now().strftime("%H:%M")
    return render(request, 'dashboard/index.html',
                  {"humidity": humidity, "temperature": temperature, "time": collectionTime})

def data(request):
    return render(request, 'dashboard/data.html')
