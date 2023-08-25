from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData
from datetime import datetime, timedelta

def collectDataIfNecessary():
    start = datetime.now - timedelta(minutes=15)
    end = datetime.now
    dataList = AirData.objects.filter(date__range=[start, end])
    if not dataList:
        AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save()