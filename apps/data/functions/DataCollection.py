from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData
from datetime import datetime

def collectDataIfNecessary():
    data = AirData.objects.all()[0]
    if data is not None:
        now = datetime.now()
        if data.date.minute != now.minute:
            AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save()