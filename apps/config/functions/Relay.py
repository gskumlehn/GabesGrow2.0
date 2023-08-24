import RPi.GPIO as GPIO
def initBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def setAsOutput(pinNumber):
    GPIO.setup(pinNumber, GPIO.OUT)

def writesToPort(pinNumber, portState):
    GPIO.output(pinNumber, portState)