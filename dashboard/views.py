from datetime import datetime
from django.shortcuts import render
from data.functions import AirHumidityAndTemperature

def index(request):
    humidity, temperature = AirHumidityAndTemperature.get()
    collectionTime = datetime.now()
    return render(request, 'dashboard/index.html',
                  {"humidity": humidity, "temperature": temperature, "time": collectionTime})


