from APScheduler.schedulers.background import BackgroundScheduler
from apps.config.functions.Watering import waterIfDryAndWateringOn

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=waterIfDryAndWateringOn,
                      trigger="cron",
                      minute="0,30",
                      second="0")
    scheduler.start()