from datetime import datetime
from django.db import models
from apps.stage.models import StageType

class GrowConfig(models.Model):
    lastUpdate = models.DateTimeField(null=False, blank=False,default=datetime.now)
    stageType = models.CharField(max_length=2, choices=StageType.choices, default=StageType.VEGETATIVE,  null=False, blank=False)
    watering = models.BooleanField(null=False, blank=False)

class GrowConfigHistory(models.Model):
    growConfig = models.ForeignKey("GrowConfig", on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False, default=datetime.now)
    description = models.TextField(null=False, blank=False)