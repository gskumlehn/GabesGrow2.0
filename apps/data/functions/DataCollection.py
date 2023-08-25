from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData
from datetime import datetime

def collectDataIfNecessary():
    start = datetime.now - datetime.timedelta(minutes=15)
    end = datetime.now
    dataList = AirData.objects.filter(date__range=[start, end])
    if not dataList:
        AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save()