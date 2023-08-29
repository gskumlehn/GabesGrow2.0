from apps.data.models import AirData
from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature

def saveAirData():
    data = AirData(humidity=getHumidity(), temperature=getTemperature())
    data.save()