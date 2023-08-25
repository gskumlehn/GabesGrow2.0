from apscheduler.schedulers.base import BaseScheduler
from apps.config.functions.Lights import lightsOnIfVegetative, lightsOffIfVegetative, lightsOnIfNotVegetative, lightsOffIfNotVegetative
def start():
    scheduler = BaseScheduler()
    scheduler.add_job(func=lightsOnIfVegetative,
                      trigger="cron",
                      minute=30,
                      hour=4)

    scheduler.add_job(func=lightsOffIfVegetative,
                      trigger="cron",
                      minute=30,
                      hour=22)

    scheduler.add_job(func=lightsOnIfNotVegetative,
                      trigger="cron",
                      minute=0,
                      hour=6)

    scheduler.add_job(func=lightsOffIfNotVegetative,
                      trigger="cron",
                      minute=0,
                      hour=18)

    scheduler.start()