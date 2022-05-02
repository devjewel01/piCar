import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

irL = 10
irR = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(irL,GPIO.IN)
GPIO.setup(irR,GPIO.IN)

def hole():
    try: 
        if GPIO.input(irL) or GPIO.input(irR):
            print("Hole found, stop car")
            return True 
        else:
            return False

    except KeyboardInterrupt:
        GPIO.cleanup()
