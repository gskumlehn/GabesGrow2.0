from datetime import datetime
from django.db import models

class AirData(models.Model):
    date = models.DateTimeField(null=False, blank=False, default=datetime.now)
    temperature = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)
    humidity = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)

class SoilData(models.Model):
    date = models.DateTimeField(null=False, blank=False, default=datetime.now)
    isWet = models.BooleanField(null=False, blank=False)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    ph = models.DecimalField(max_digits=5, decimal_places=2)