from apscheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.AirHumidityAndTemperature import get
from apps.data.models import AirData

def start():
    scheduler = BackgroundScheduler
    humidity, temperature = get()
    scheduler.add_job(func=AirData.objects.create(humidity=humidity, temperature=temperature).save(),
                      trigger="interval",
                      minutes=1,
                      replace_existing=True)
    scheduler.start()
