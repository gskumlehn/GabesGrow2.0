import RPi.GPIO as GPIO

lightRelayPort = 4
def initBoard():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def setAsOutput(pinNumber):
    GPIO.setup(pinNumber, GPIO.OUT)

def writesToPort(pinNumber, portState):
    GPIO.output(pinNumber, portState)

def lightsOn():
    initBoard()
    setAsOutput(lightRelayPort)
    writesToPort(lightRelayPort, 0)

def lightsOff():
    initBoard()
    setAsOutput(lightRelayPort)
    writesToPort(lightRelayPort, 1)