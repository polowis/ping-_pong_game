"""
FINAL VERSION:
@author polowis


This code is for paddle movement, you may add some additional functions if needed.
Check the code for ball movement "ball4.py"



"""
from microbit import *

class Paddle:
    def __init__(self, rightPaddle, leftPaddle):
        self.rightPaddle = rightPaddle
        self.leftPaddle = leftPaddle


    def __setPaddleLeft(self):
        display.set_pixel(self.leftPaddle, 0, 5)
        display.set_pixel((self.leftPaddle - 1), 0, 5)

    def __setPaddleRight(self):
        display.set_pixel(self.rightPaddle, 4, 5)
        display.set_pixel((self.leftPaddle - 1), 4, 5)

    def start(self):
        self.__setPaddleLeft()
        self.__setPaddleRight()

    def setPaddle(self, rightPaddle, leftPaddle):

        self.rightPaddle += button_b.get_presses()
        self.rightPaddle -= button_b.get_presses()
        if self.rightPaddle < 1:
            self.rightPaddle = 1
        elif self.rightPaddle > 4:
            self.rightPaddle = 4
        return
        
        
        
        
        
        
        
