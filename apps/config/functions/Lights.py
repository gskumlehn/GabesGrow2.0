from apps.config.functions import Relay
from apps.config.models import GrowConfig
from apps.stage.models import StageType

lightRelayPort = 8

def lightsOn():
    Relay.initBoard()
    Relay.setAsOutput(lightRelayPort)
    Relay.writesToPort(lightRelayPort, 1)

def lightsOff():
    Relay.initBoard()
    Relay.setAsOutput(lightRelayPort)
    Relay.writesToPort(lightRelayPort, 0)

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