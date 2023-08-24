from apps.config.functions import Relay

lightRelayPort = 8

def lightsOn():
    Relay.initBoard()
    Relay.setAsOutput(lightRelayPort)
    Relay.writesToPort(lightRelayPort, 1)

def lightsOff():
    Relay.initBoard()
    Relay.setAsOutput(lightRelayPort)
    Relay.writesToPort(lightRelayPort, 0)