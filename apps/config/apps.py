from django.apps import AppConfig


class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.config'

    def ready(self):
        from apps.config.scheduler import LightsScheduler, WateringScheduler, DataCollectionScheduler
        LightsScheduler.start()
        WateringScheduler.start()
        DataCollectionScheduler.start()
