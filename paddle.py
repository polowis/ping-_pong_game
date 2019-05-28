class Paddle():
    def setPaddleLeft(self):
        display.set_pixel(4, 0, 9)
        display.set_pixel(4, 1, 9)
    def setPaddleRight(self):
        display.set_pixel(0, 4, 9)
        display.set_pixel(0, 3, 9)
