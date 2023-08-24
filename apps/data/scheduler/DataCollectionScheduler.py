from apscheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.AirHumidityAndTemperature import getHumidity, getTemperature
from apps.data.models import AirData

def start():
    scheduler = BackgroundScheduler
    scheduler.addJob(AirData(humidity=getHumidity(), temperature=getTemperature()).save(), "interval", minutes=1, replace_existing=True)
    scheduler.start()
}