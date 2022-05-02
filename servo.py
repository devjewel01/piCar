import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

servoUltraSonicPin = 17
servoCameraUpDownPin = 21
servoCameraLeftRightPin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoUltraSonicPin, GPIO.OUT)
GPIO.setup(servoCameraUpDownPin, GPIO.OUT)
GPIO.setup(servoCameraLeftRightPin, GPIO.OUT)

servoUltraSonic = GPIO.PWM(servoUltraSonicPin, 50)
servoCameraUpDown = GPIO.PWM(servoCameraUpDownPin, 50)
servoCameraLeftRight = GPIO.PWM(servoCameraLeftRightPin, 50)

servoUltraSonic.start(7)
servoCameraUpDown.start(6.5)
servoCameraLeftRight.start(7.5) 
time.sleep(0.1)


def ultraSonicLeft():
  servoUltraSonic.ChangeDutyCycle(11)

def ultraSonicRight():
  servoUltraSonic.ChangeDutyCycle(3)

def ultraSonicPosition():
  servoUltraSonic.ChangeDutyCycle(7)

def cameraUp():
  servoCameraUpDown.ChangeDutyCycle(10)

def cameraDown():
  servoCameraUpDown.ChangeDutyCycle(4)

def cameraLeft():
  servoCameraLeftRight.ChangeDutyCycle(11)

def cameraRight():
  servoCameraLeftRight.ChangeDutyCycle(4)

def cameraPosition():
  servoCameraLeftRight.ChangeDutyCycle(7.5)
  servoCameraUpDown.ChangeDutyCycle(6.5)


