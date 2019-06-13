
"""
4.0.0
This is the final version of the ball movement, this WILL work. I will explain how to make this code work in the class
If you're reading this, I just want to tell you, we nearly finish the assignment :)) (need to add scoring system and some other functions
but thats ok). I have TESTED the code. but some minor bugs may occur.

The code for paddle movement will be on the other file. 
HAPPY CODING :> 

4.1.0
OOP version and non OOP version. Please use OOP version instead. Both versions have the same result, just different style of writing
I have decided to combine movement paddle. Please use the class Ball code when submitting the assignment. 


"""

from microbit import *
import music
import random


class Ball:
    def __init__(self, x = 2, y = 2, xspeed = (random.choice([-1, 1])), yspeed = (random.choice([-1, 1]))):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.bottomPaddle = 1
        self.topPaddle = 1
        self.yspeed = (random.choice([-1, 1]))
        self.xspeed = (random.choice([-1, 1]))

    def __setPaddleTop(self):
        display.set_pixel(self.topPaddle, 0, 5)
        display.set_pixel((self.topPaddle - 1), 0, 5)

    def __setPaddleBottom(self):
        display.set_pixel(self.bottomPaddle, 4, 5)
        display.set_pixel(self.bottomPaddle - 1, 4, 5)

    def __getCurrentBallPosition(self):
        return self.x, self.y

    def setPaddle(self):
        self.bottomPaddle += button_b.get_presses()
        self.bottomPaddle -= button_b.get_presses()
        if self.bottomPaddle < 1:
            self.bottomPaddle = 1
        elif self.bottomPaddle > 4:
            self.bottomPaddle = 4
        return

    def show(self):
        display.clear()
        self.__setPaddleTop()
        self.__setPaddleBottom()
        display.set_pixel(self.x, self.y, 9)
        sleep(1000)
        

    def AI(self):
        if (random.randint(1, 6)) != 1:
            if self.x < self.topPaddle - 1:
                self.topPaddle = self.topPaddle -1
            elif self.x > self.topPaddle:
                self.topPaddle = self.topPaddle + 1
              
    def render(self):
      self.__getCurrentBallPosition()
      display.set_pixel(self.x, self.y, 9)
      sleep(500)
      display.set_pixel(self.x, self.y, 0)
      sleep(500)
    
        
    def update(self):
        if self.y == 2:
            self.x = self.x + self.yspeed
            self.y = self.y + self.yspeed
        elif self.y == 1 or self.y == 3:
            if self.y == 1:
                if self.topPaddle == self.x:
                    self.xspeed = 1
                    self.yspeed = 1
                elif self.topPaddle - 1 == self.x:
                    self.xspeed = -1
                    self.yspeed = 1
            else:
                if self.bottomPaddle == self.x:
                    self.xspeed = 1
                    self.yspeed = -1
                elif self.bottomPaddle - 1 == self.x:
                    self.xspeed = -1
                    self.yspeed = -1
            self.x += self.xspeed
            self.y += self.yspeed
            
        else:
            self.x += self.xspeed
            self.y += self.yspeed
        if self.x <= 0 or self.x >= 4:
            self.xspeed = self.xspeed * -1
        if self.y <= 0:
            return 1
        elif self.y >= 4:
            return 2
        else:
            return 0


          
          
ball = Ball()

def function():
     ball.setPaddle()
     ball.AI()
     edges = ball.update()


ball.show()
sleep(500)
while True:
     function()
     ball.show()
     if ball.update() != 0:
        break
        sleep(500)
if ball.update() == 1:
    display.show(Image.HAPPY)
elif ball.update() == 2:
    display.show(Image.SAD)


        
        

          

