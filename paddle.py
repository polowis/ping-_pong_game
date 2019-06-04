class Paddle():
    def __init__(self, x1, x2 , y1, y2 ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def setPaddleRight(self):
        self.x1 = 4
        self.x2 = 4
        self.y1 = 0
        self.y2 = 1
        display.set_pixel(self.x1, self.y1, 9)
        display.set_pixel(self.x2, self.y2, 9)

    def setPaddleLeft(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 4
        self.y2 = 3
        display.set_pixel(self.x1, self.y1, 9)
        display.set_pixel(self.x2, self.y2, 9)

    def startGame(self):
        self.setPaddleLeft()
        self.setPaddleRight()

    def moveUp(self):
        self.y1 -= 1
        self.y2 -= 1
        if self.y1 or self.y2 == 0:
            return self.y1, self.y2

    def moveDown(self):
        self.y += 1
        self.y += 1
        if self.y1 or self.y2 == 0:
            return self.y1, self.y2
            


    def getCurrentPosition(self):
        return self.x1, self.y1, self.x2, self.y2


    def update(self):
        display.set_pixel(self.x1, self.y1, 9)
        display.set_pixel(self.x2, self.y2, 9)

