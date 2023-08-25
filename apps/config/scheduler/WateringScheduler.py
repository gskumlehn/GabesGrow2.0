from apscheduler.schedulers.background import BackgroundScheduler
from apps.config.functions import Watering

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=Watering.waterIfDry(),
                      trigger="interval",
                      minutes=30)
    scheduler.start()