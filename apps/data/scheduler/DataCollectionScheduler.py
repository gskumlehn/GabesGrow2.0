from apscheduler.schedulers.background import BackgroundScheduler
from apps.data.functions.DataCollection import collectDataIfNecessary

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=collectDataIfNecessary,
                      trigger="cron",
                      minute="0,30,42,43,44")
    scheduler.start()
