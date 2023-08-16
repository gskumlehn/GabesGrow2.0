from django.db import models

class AirData(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    temperature = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)
    humidity = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)

class SoilData(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    humidity = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)

class GrowConfig(models.Model):
    lastUpdate = models.DateTimeField(null=False, blank=False)
    stage = models.CharField(max_length=10, null=False, blank=False)
    watering = models.BooleanField(null=False, blank=False)
class GrowConfigHistory(models.Model):
    growConfig = models.ForeignKey("GrowConfig", on_delete=models.CASCADE)
