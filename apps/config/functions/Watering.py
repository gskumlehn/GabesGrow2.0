from apps.config.functions import Relay
from time import sleep

wateringRelayPort = 10
waterSensorPort = 22

def wateringOn():
    Relay.writesToPort(wateringRelayPort, 0)

def wateringOff():
    Relay.writesToPort(wateringRelayPort, 1)

def waterFor(seconds):
    Relay.initBoard()
    Relay.setAsOutput(wateringRelayPort)
    wateringOn()
    sleep(seconds)
    wateringOff()

def waterIfDry():
    Relay.initBoard()
    Relay.setAsInput(waterSensorPort)
    if Relay.readsPort(waterSensorPort):
        waterFor(5)
