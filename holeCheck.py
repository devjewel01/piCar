from buzzer import  alert
from ir import hole
from time import sleep
from motor import Forward, Stop

def holeFound():
    if not hole():
        alert()
        sleep(0.5)

while True:
    if hole():
        Forward(15)
    else:
        Stop() 
        alert()
        sleep(0.5)
