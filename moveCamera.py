#!/usr/bin/env python3

import readchar
from servo import cameraLeftRight, cameraUpDown, cameraPosition

x = 7.5
y = 6.5

def getch():
   ch = readchar.readchar()
   return ch



while True:
   char = getch()
   
   if(char == "w"):
      y += 0.5 
      if y>13:
         y = 13
      if y<0:
         y = 0
      cameraUpDown(y)

   if(char == "s"):
      y -= 0.5 
      if y>13:
         y = 13
      if y<0:
         y = 0
      cameraUpDown(y)

   if(char == "d"):      
      x -= 0.5
      if x>13:
         x = 13
      if x<0:
         x = 0
      cameraLeftRight(x)

   if(char == "a"):
      x += 0.5
      if x>13:
         x = 13
      if x<0:
         x = 0
      cameraLeftRight(x)

   if(char == "x"):
      x = 7.5
      y = 6.5
      cameraPosition()
   
   char = ""