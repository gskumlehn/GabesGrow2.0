from datetime import datetime
from django.shortcuts import render
from growweb.functions.AirHumidityAndTemperature import AirHumidityAndTemperature

def index(request):
    humidity, temperature = AirHumidityAndTemperature.get()
    collectionTime = datetime.datetime.now()
    return render(request, 'growweb/index.html', {"humidity": humidity, "temperature": temperature, "time": collectionTime})
def data(request):
    return render(request, 'growweb/data.html')
