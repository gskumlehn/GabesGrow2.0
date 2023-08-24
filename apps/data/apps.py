from django.apps import AppConfig
from apps.data.scheduler import DataCollectionScheduler

class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.data'

    def ready(self):
        DataCollectionScheduler.start()

