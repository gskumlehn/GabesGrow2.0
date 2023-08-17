from datetime import datetime
from django.shortcuts import render

def index(request):
    humidity, temperature = 70, 22
    collectionTime = datetime.now()
    return render(request, 'dashboard/index.html',
                  {"humidity": humidity, "temperature": temperature, "time": collectionTime})


