from apscheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.DataService import saveAirData

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=saveAirData,
                      trigger="cron",
                      second="0")
    scheduler.start()
