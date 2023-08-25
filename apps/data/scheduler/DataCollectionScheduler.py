from apscheduler.schedulers.base import BaseScheduler
from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData

def start():
    scheduler = BaseScheduler()
    scheduler.add_job(func=AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save,
                      trigger="interval",
                      minutes=30)
    scheduler.start()
