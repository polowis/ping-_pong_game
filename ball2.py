"""
V2.0.0 feel free to look at v1.0.0
"""

class Ball:
    def __init__(self, x=2, y=2, xspeed = 1, yspeed = 1):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    def show(self):
        display.set_pixel(self.x, self.y, 9)
        sleep(100)
        display.set_pixel(self.x, self.y, 0)
    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
    def edges(self):
      if self.y < 0 or self.y > 4:
        self.yspeed == 0
      if self.x > 4 or self.x < 0: 
        self.xspeed -= 1
        
 
