from apscheduler.schedulers.background import BackgroundScheduler
from apps.config.functions.Watering import waterIfDry

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=waterIfDry,
                      trigger="cron",
                      minute="0,30",
                      second="0")
    scheduler.start()