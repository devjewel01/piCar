#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


Motor1 = {'EN': 26, 'input1': 19, 'input2': 13}
Motor2 = {'EN': 16, 'input1': 6, 'input2': 5}

for x in Motor1:
    GPIO.setup(Motor1[x], GPIO.OUT)
    GPIO.setup(Motor2[x], GPIO.OUT)

EN1 = GPIO.PWM(Motor1['EN'], 100)    
EN2 = GPIO.PWM(Motor2['EN'], 100)    

EN1.start(0)                    
EN2.start(0)  


def Run(a, b, c, d, x):
    GPIO.output(Motor1['input1'], GPIO.LOW)
    GPIO.output(Motor1['input2'], GPIO.LOW)
    GPIO.output(Motor2['input1'], GPIO.LOW)
    GPIO.output(Motor2['input2'], GPIO.LOW)

    if a==1:
        GPIO.output(Motor1['input1'], GPIO.HIGH)
    if b==1:
        GPIO.output(Motor1['input2'], GPIO.HIGH)
    if c==1:
        GPIO.output(Motor2['input1'], GPIO.HIGH)
    if d==1:
        GPIO.output(Motor2['input2'], GPIO.HIGH)

    EN1.ChangeDutyCycle(x)
    EN2.ChangeDutyCycle(x)
    


def Stop():
    Run(0,0,0,0,0)

def Start_Slow(a, b, c, d):
    for i in range(0,100,20):
        Run(a,b,c,d,i)
        time.sleep(0.5)
    
def Stop_Slow(a,b,c,d):
    for i in range(100,0,-20):
        Run(a,b,c,d,i)
        time.sleep(0.5)


def Forward(x=50):
    Run(1,0,1,0,x)

def Backward(x=50):
    Run(0,1,0,1,x)

def Left(x=50):
    Run(0,1,1,0,x)

def Right(x=50):
    Run(1,0,0,1,x)

def littleForward(x=50):
    Run(1,0,1,0,x)
    time.sleep(0.5)
    Stop()


def littleBackward(x=50):
    Run(0,1,0,1,x)
    time.sleep(0.5)
    Stop()

def littleLeft(x=50):
    Run(0,1,1,0,x)
    time.sleep(0.3)
    Stop()

def littleRight(x=50):
    Run(1,0,0,1,x)
    time.sleep(0.3)
    Stop()

def Start():
    Start_Slow(1,0,1,0)

def StopSlowly():
    Stop_Slow(1,0,1,0)


def setMotorLeft(power):
   GPIO.output(Motor1['input1'], GPIO.LOW)
   GPIO.output(Motor1['input2'], GPIO.LOW)

   int(power)
   if power > 0:
      pwm = int(100 * power)
      if pwm > 100:
         pwm = 100
      GPIO.output(Motor1['input1'], GPIO.HIGH)
      EN1.ChangeDutyCycle(pwm)
      	  
   elif power < 0:
      pwm = -int(100 * power)
      if pwm > 100:
         pwm = 100
      GPIO.output(Motor1['input2'], GPIO.HIGH)
      EN1.ChangeDutyCycle(pwm)
    

def setMotorRight(power):
   GPIO.output(Motor2['input1'], GPIO.LOW)
   GPIO.output(Motor2['input2'], GPIO.LOW)

   int(power)
   if power > 0:
      pwm = int(100 * power)
      if pwm > 100:
         pwm = 100
      GPIO.output(Motor2['input1'], GPIO.HIGH)
      EN2.ChangeDutyCycle(pwm)

   elif power < 0:
      pwm = -int(100 * power)
      if pwm > 100:
         pwm = 100
      GPIO.output(Motor2['input2'], GPIO.HIGH)
      EN2.ChangeDutyCycle(pwm)
    
def exit():
    GPIO.output(Motor1['input1'], GPIO.LOW)
    GPIO.output(Motor1['input2'], GPIO.LOW)
    GPIO.output(Motor2['input1'], GPIO.LOW)
    GPIO.output(Motor2['input2'], GPIO.LOW)

    GPIO.cleanup()
