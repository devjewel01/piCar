import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

irL = 9
irM = 11
irR = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(irL,GPIO.IN)
GPIO.setup(irR,GPIO.IN)
GPIO.setup(irM,GPIO.IN)


def hole():
    try: 
        if GPIO.input(irL) or GPIO.input(irM) or GPIO.input(irR):
            print("Hole found, stop car")
            return True 
        else:
            return False

    except KeyboardInterrupt:
        GPIO.cleanup()

def leftSensor():
    return GPIO.input(irL)

def rightSensor():
    return GPIO.input(irR)

def middleSensor():
    return GPIO.input(irM)