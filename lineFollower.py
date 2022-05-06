from motor import Forward, Backward, Left, Right, Stop
from ir import leftSensor, middleSensor, rightSensor
import time 

def lineCheck():
    if leftSensor() and rightSensor() and not middleSensor():
        Forward(28)
    elif not leftSensor() and rightSensor():
        Left(60)
    elif leftSensor() and not rightSensor():
        Right(60)
    elif middleSensor():
        Stop()

while True:
    lineCheck()
