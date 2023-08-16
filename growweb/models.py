from django.db import models
from datetime import datetime

class AirData(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    temperature = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)
    humidity = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)

class SoilData(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    humidity = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)

class StageType(models.TextChoices):
    VEGETATIVE = "VG", "Vegetative"
    FLOWERING = "FL", "Flowering"

class GrowConfig(models.Model):
    lastUpdate = models.DateTimeField(null=False, blank=False,default=datetime.now)
    stageType = models.CharField(max_length=2, choices=StageType.choices, default=StageType.VEGETATIVE,  null=False, blank=False)
    watering = models.BooleanField(null=False, blank=False)

class Stage(models.Model):
    type = models.CharField(max_length=2, choices=StageType.choices, null=False, blank=False)
    lightOn = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    lightOff = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    phMin = models.DecimalField(max_digits=4, decimal_places=2)
    phMax = models.DecimalField(max_digits=4, decimal_places=2)
    tempMin = models.DecimalField(max_digits=4, decimal_places=2)
    tempMax = models.DecimalField(max_digits=4, decimal_places=2)
    soilHumMin = models.DecimalField(max_digits=4, decimal_places=2)
    soilHumMax = models.DecimalField(max_digits=4, decimal_places=2)
    airHumMin = models.DecimalField(max_digits=4, decimal_places=2)
    airHumMax = models.DecimalField(max_digits=4, decimal_places=2)

class GrowConfigHistory(models.Model):
    growConfig = models.ForeignKey("GrowConfig", on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False, default=datetime.now)
    description = models.TextField(null=False, blank=False)
