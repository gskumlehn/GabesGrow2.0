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
    config = GrowConfig.objects.get(1)
    if config.stageType == StageType.VEGETATIVE:
        lightsOn()

def lightsOnIfNotVegetative():
    config = GrowConfig.objects.get(1)
    if config.stageType != StageType.VEGETATIVE:
        lightsOn()
def lightsOffIfVegetative():
    config = GrowConfig.objects.get(1)
    if config.stageType == StageType.VEGETATIVE:
        lightsOff()

def lightsOffIfNotVegetative():
    config = GrowConfig.objects.get(1)
    if config.stageType != StageType.VEGETATIVE:
        lightsOff()