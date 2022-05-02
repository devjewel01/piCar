from buzzer import  alert
from ir import hole
from time import sleep

def holeFound():
    if hole():
        alert()
        sleep(0.5)



