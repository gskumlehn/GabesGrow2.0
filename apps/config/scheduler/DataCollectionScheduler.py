from APScheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.DataService import saveAirData

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=saveAirData,
                      trigger="cron",
                      minute="0,30",
                      second="0")
    scheduler.start()
