'''
v3.0.0
@author Polowis

this code works better than the other two, but still results in run time error: maximum recursion depth exceeded because we're using 
tail recrusion in the code because python prevents inifinte recursions to avoid stack overflow. 
V3.0.0 improves the caculation for the ball direction by adding some maths. 

There are a few ways to fix this problem:
use setrecursionlimit() to increase the value of recursion limit but this is dangerous because
it will change the memory allocation space for stack which is responsible for storing values of programming counter during recursion process
or we can do it manually to bounce the ball which is not recommended.

Because the ball need to bounce infinitely, I cannot figure out any other ways to perform this without using recursion. 
P/S This piece of code work perfecly in processing programming language. However, some adjustments have been made so it
can work with microbit. 
'''

from microbit import *
import math        
import random
   
class Ball:
    def __init__(self, x=2, y=2, xspeed = 1, yspeed = 1):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.reset()
    def reset(self):
        self.x = 2
        self.y = 2
        angle = int(random.uniform(- math.pi / 4, math.pi / 4))
        self.xspeed = 2 * math.cos(angle)
        self.yspeed = 2 * math.sin(angle)
        if random.random() < 0.5:
          self.xspeed *= -1
        
    def show(self):
        display.set_pixel(int(self.x), int(self.y), 9)
        sleep(100)
        display.set_pixel(int(self.x), int(self.y), 0)
    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
    def edges(self):
      if self.y < 0:
        self.yspeed *= -1
      if self.y > 4:
        self.yspeed *= 1
      if self.x > 4 or self.x < 0: 
        self.reset()
