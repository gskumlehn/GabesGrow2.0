from apscheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData

def start():
    scheduler = BackgroundScheduler
    scheduler.add_job(AirData(humidity=getHumidity(), temperature=getTemperature()).save(), "interval", minutes=1, replace_existing=True)
    scheduler.start()
