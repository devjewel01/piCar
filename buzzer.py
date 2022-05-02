from gpiozero import LED
from signal import pause
from time import sleep

buzzer = LED(18)

def Buzzer():
    buzzer.on()
    sleep(1)
    buzzer.off()

def blink():
    buzzer.on()
    sleep(0.1)
    buzzer.off()
    sleep(0.1)

def alert():
    blink()
    blink()
    blink()


