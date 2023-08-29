from apps.config.functions import Pinout
from apps.config.models import GrowConfig

lightRelayPort = 14

def lightsOn():
    Pinout.initBoard()
    Pinout.setAsOutput(lightRelayPort)
    Pinout.writesToPort(lightRelayPort, 1)

def lightsOff():
    Pinout.initBoard()
    Pinout.setAsOutput(lightRelayPort)
    Pinout.writesToPort(lightRelayPort, 0)

def lightsOnIfVegetative():
    config = GrowConfig.objects.get(id=1)
    if config.stageType == "VG":
        config.lights = True
        config.save()
        lightsOn()

def lightsOffIfVegetative():
    config = GrowConfig.objects.get(id=1)
    if config.stageType == "VG":
        config.lights = False
        config.save()
        lightsOff()

def lightsOnIfNotVegetative():
    config = GrowConfig.objects.get(id=1)
    if config.stageType != "VG":
        config.lights = True
        config.save()
        lightsOn()

def lightsOffIfNotVegetative():
    config = GrowConfig.objects.get(id=1)
    if config.stageType != "VG":
        config.lights = False
        config.save()
        lightsOff()