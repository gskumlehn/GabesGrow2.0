import RPi.GPIO as GPIO
def initBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def setAsInput(pinNumber):
    GPIO.setup(pinNumber, GPIO.IN)

def setAsOutput(pinNumber):
    GPIO.setup(pinNumber, GPIO.OUT)

def readsPort(pinNumber):
    GPIO.input(pinNumber)

def writesToPort(pinNumber, portState):
    GPIO.output(pinNumber, portState)