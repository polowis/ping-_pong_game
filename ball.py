class Ball:
    def __init__(self, x=2, y=2):
        self.x = x
        self.y = y
    def startTheGame(self):
        display.set_pixel(self.x, self.y, 9)
        display.set_pixel(self.x, self.y, 9)
        
    '''
    Use recursive algorithm to move the position of the ball
    '''
        
