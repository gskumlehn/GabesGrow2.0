from apps.config.functions import Pinout
from apps.config.models import GrowConfig
from time import sleep

wateringRelayPort = 15
waterSensorPort = 24

def wateringOn():
    Pinout.writesToPort(wateringRelayPort, 0)

def wateringOff():
    Pinout.writesToPort(wateringRelayPort, 1)

def waterFor(seconds):
    Pinout.initBoard()
    Pinout.setAsOutput(wateringRelayPort)
    wateringOn()
    sleep(seconds)
    wateringOff()

def waterIfDryAndWateringOn:
    config = GrowConfig.objects.get(id=1)
    if (config.watering):
        waterIfDry()

def waterIfDry():
    if True:
        waterFor(5)

def isDry():
    Pinout.initBoard()
    Pinout.setAsInput(waterSensorPort)
    return Pinout.readsPort(waterSensorPort)