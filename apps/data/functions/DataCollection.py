from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData
from datetime import datetime

def collectDataIfNecessary():
    data = AirData.objects.filter(date=datetime.now())
    if data is None:
        AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save()