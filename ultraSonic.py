from gpiozero import DistanceSensor

sensor = DistanceSensor(24, 23) #echo - trigger

def Distance():
    # print('Distance to nearest object is', sensor.distance, 'm')
    return sensor.distance
