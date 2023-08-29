from apscheduler.schedulers.background import BackgroundScheduler
from apps.config.functions.Watering import waterIfDryAndWateringOn

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=waterIfDryAndWateringOn,
                      trigger="cron",

                      second="0")
    scheduler.start()