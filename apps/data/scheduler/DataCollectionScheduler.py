from apscheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=AirData.objects.create(humidity=getHumidity(), temperature=getTemperature()).save,
                      trigger="cron",
                      minutes="0/30",
                      replace_existing=True)
    scheduler.start()
