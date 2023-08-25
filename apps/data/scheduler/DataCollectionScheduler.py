from apscheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save,
                      trigger="interval",
                      minutes="30")
    scheduler.start()
