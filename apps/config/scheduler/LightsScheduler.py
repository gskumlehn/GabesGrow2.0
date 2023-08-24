from apscheduler.schedulers.background import BackgroundScheduler
from apps.config.functions.Lights import lightsOnIfVegetative, lightsOffIfVegetative, lightsOnIfNotVegetative, lightsOffIfNotVegetative
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lightsOnIfVegetative,
                      trigger="cron",
                      minute=0,
                      hour=6,
                      replace_existing=True)

    scheduler.add_job(func=lightsOffIfVegetative,
                      trigger="cron",
                      minute=0,
                      hour=18,
                      replace_existing=True)
    scheduler.add_job(func=lightsOnIfNotVegetative,
                      trigger="cron",
                      minute=30,
                      hour=4,
                      replace_existing=True)

    scheduler.add_job(func=lightsOffIfNotVegetative,
                      trigger="cron",
                      minute=30,
                      hour=18,
                      replace_existing=True)
    scheduler.start()