from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData
from datetime import datetime, timedelta

def collectDataIfNecessary():
    end = datetime.now()
    start = end - timedelta(minutes=15)
    dataList = AirData.objects.filter(date__range=[start, end])
    if not dataList:
        AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save()