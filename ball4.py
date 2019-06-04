



from microbit import *
import random
  
class Ball:
    def __init__(self, x = 2, y = 2, xspeed = (random.choice([-1, 1])), yspeed = (random.choice([-1, 1]))):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        
        self.rightPaddle = 1
        self.leftPaddle = 1
    def __getBallLocation(self):
      return self.x, self.y
    def startGame(self):
       display.set_pixel(self.x, self.y, 9)
       sleep(500)
       display.set_pixel(self.x, self.y, 0)
       sleep(500)
    def edges(self):
      global edge
      edge = self.__update()
      if edge == 1:
        display.show(Image.HAPPY)
      elif edge == 2:
        display.show(Image.SAD)
    def show(self):
        display.clear()
        
        display.set_pixel(self.x, self.y, 9)
        return
    def __update(self):
        if self.y == 2:
            self.x = self.x + self.yspeed
            self.y = self.y + self.yspeed
        elif self.y == 1 or self.y == 3:
            if self.y == 1:
                if self.leftPaddle == self.x:
                    self.xspeed = -1
                    self.yspeed = -1
                elif self.leftPaddle - 1 == self.x:
                    self.xspeed = -1
                    self.yspeed = -1
            else:
                if self.rightPaddle == self.x:
                    self.xspeed = 1
                    self.yspeed = -1
                elif self.rightPaddle - 1 == self.x:
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
