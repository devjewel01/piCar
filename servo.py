import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

servoUltraSonicPin = 17
servoCameraUpDownPin = 20
servoCameraLeftRightPin = 21

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
  servoUltraSonic.ChangeDutyCycle(13)

def ultraSonicRight():
  servoUltraSonic.ChangeDutyCycle(3)

def ultraSonicPosition():
  servoUltraSonic.ChangeDutyCycle(8)

def cameraUp():
  servoCameraUpDown.ChangeDutyCycle(9)

def cameraDown():
  servoCameraUpDown.ChangeDutyCycle(5)

def cameraLeft():
  servoCameraLeftRight.ChangeDutyCycle(13)

def cameraRight():
  servoCameraLeftRight.ChangeDutyCycle(3)

def cameraPosition():
  servoCameraLeftRight.ChangeDutyCycle(7.5)
  servoCameraUpDown.ChangeDutyCycle(6.5)

def cameraUpDown(x):
  if x>13:
    x = 13
  if x<0:
    x = 0
  servoCameraUpDown.ChangeDutyCycle(x)

def cameraLeftRight(x):
  if x>13:
    x = 13
  if x<0:
    x = 0
  servoCameraLeftRight.ChangeDutyCycle(x)
