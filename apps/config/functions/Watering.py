from apps.config.functions import Relay
from time import sleep

lightRelayPort = 10

def wateringOn():
    Relay.writesToPort(lightRelayPort, 0)

def wateringOff():
    Relay.writesToPort(lightRelayPort, 1)

def waterFor(seconds):
    Relay.initBoard()
    Relay.setAsOutput(lightRelayPort)
    wateringOn()
    sleep(seconds)
    wateringOff()