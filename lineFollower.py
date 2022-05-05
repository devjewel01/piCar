from turtle import left, right
from motor import Forward, Backward, Left, Right, Stop
from ir import leftSensor, middleSensor, rightSensor

def lineCheck():
    if leftSensor() and rightSensor() and not middleSensor:
        Forward(20)
    elif not leftSensor() and rightSensor():
        Left(30)
    elif leftSensor() and not rightSensor():
        Right(30)
    else:
        Stop()
    
