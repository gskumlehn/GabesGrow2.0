from apscheduler.schedulers.base import BaseScheduler
from apps.config.functions import Watering

def start():
    scheduler = BaseScheduler()
    scheduler.add_job(func=Watering.waterIfDry(),
                      trigger="interval",
                      minutes=30)
    scheduler.start()