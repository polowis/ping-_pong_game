class Ball:
    def __init__(self, x=2, y=2):
        self.x = x
        self.y = y
    def startTheGame(self):
        display.set_pixel(self.x, self.y, 9)
        display.set_pixel(self.x, self.y, 9)
        
    '''
    Use recursive algorithm to move the position of the ball
    This will likely result in stack overflow, since the ball will need to move infinitely until one player lose. 
    This piece of code uses tail recursion, it will run until it reaches the maximum recursion loops
    '''
    def update(self, x=2, y=2, z=0):
        z += 1
        display.set_pixel(self.x, self.y, 9)
        sleep(500)
        display.set_pixel(self.x, self.y, 0)
        if z <= 200:
          if self.x == 4:
            self.x -= 1
            self.y += 1
          elif self.y == 0:
            self.y += 1
            self.x -= 1
          else:
            self.x += 1
            self.y -= 1
        self.update(self.x, self.y, z)
        
