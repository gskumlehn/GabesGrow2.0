from apps.config.functions import Pinout
from time import sleep

wateringRelayPort = 10
waterSensorPort = 18

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

def waterIfDry():
    if isDry():
        waterFor(5)

def isDry():
    Pinout.initBoard()
    Pinout.setAsInput(waterSensorPort)
    return bool(Pinout.readsPort(waterSensorPort))