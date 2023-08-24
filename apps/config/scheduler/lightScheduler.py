from apscheduler.schedulers.background import BackgroundScheduler
from apps.config.models import GrowConfig

def start():
    scheduler = BackgroundScheduler
    config = GrowConfig.objects.get(id=1)
    scheduler.addJob(config.lightOn, "interval")

}