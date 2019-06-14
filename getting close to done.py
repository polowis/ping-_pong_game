from microbit import *
import music
import random
import radio

radio.on()
radio.config(channel = 23) #The channel makes sure that the code is received without being lost and mixed up with other radio signals.

#group all the functions in a class, easier to maintain and structure the code. 
#camel style for naming convetion :). 
class Ball:
    #create a constructor, takes 4 parameters
    #the x and y coordinates gives position of the ball. 
    #xspeed and yspeed are random values which determine the movement of the ball.
    #here, self is the instance of the class
    def __init__(self, x = 2, y = 2, xspeed = (random.choice([-1, 1])), yspeed = (random.choice([-1, 1]))): 
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.bottomPaddle = 1
        self.topPaddle = 
        
    #set the top paddle at specific position.
    #paddle has 2 pixels, displaying on the top of the x-axis. 
    #set this to private method, so it cannot be accessed outside of the class
    def __setPaddleTop(self):
        display.set_pixel(self.topPaddle, 0, 5) 
        display.set_pixel((self.topPaddle - 1), 0, 5) 
    
    #set the bottom padde
    #paddle has 2 pixels, displaying on the bottom of the x-axis
    #again, set this method to private, so it cannot be accessed outside of the class
    def __setPaddleBottom(self):
        display.set_pixel(self.bottomPaddle, 4, 5)
        display.set_pixel((self.bottomPaddle - 1), 4, 5)
    
    #return the x and y value of the ball
    def __getCurrentBallPosition(self):
        return self.x, self.y
    
    #check condition of the paddle, if bottom paddle position less than 1, assign 1 to its value
    #prevents index out of bounds
    def __getSetPaddle(self):
        if self.bottomPaddle < 1:
            self.bottomPaddle = 1
        elif self.bottomPaddle > 4:
            self.bottomPaddle = 4
    
    #the setPaddle method takes 1 parameter which is the message
    def setPaddle(self, message): #(SetPaddle) reads the message that is sent from the movement microbit and is used to move the paddle either left or right.
        if message == "right":
            self.bottomPaddle += 1
            #move the paddle by one according to the message
        elif message == "left":
            self.bottomPaddle -= 1
        self.__getSetPaddle()
        return
    
    #display all the paddle, use private method setPaddleTop and setPaddleBottom
    def show(self):
        display.clear()
        self.__setPaddleTop()
        self.__setPaddleBottom()
        display.set_pixel(self.x, self.y, 9)
        sleep(500)
        

    def AI(self): #The AI is displayed on the top of the microbit display and reacts to the movement of the ball and this is what the player is playing against.
        if (random.randint(1, 6)) != 1:
            #move the top padding according to the ball position
            if self.x < self.topPaddle - 1:
                self.topPaddle = self.topPaddle -1
            elif self.x > self.topPaddle:
                self.topPaddle = self.topPaddle + 1
    
    #render the ball on the microbit
    def render(self):
      self.__getCurrentBallPosition() #this is for debugging, to make sure the ball doesnt go out of bounds. 
      #if no errors occur, display the ball.
      display.set_pixel(self.x, self.y, 9) 
      sleep(1000)
      display.set_pixel(self.x, self.y, 0)
      sleep(1000)
    
    #up    
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
     message = radio.receive()
     ball.setPaddle(message)
     ball.AI()
     edges = ball.update()


ball.show()
sleep(500)
while True: #Main Loop
     function()
     ball.show()
     if ball.update() != 0:
        break
        sleep(500)
if ball.update() == 1:
    display.show(Image.HAPPY)
elif ball.update() == 2:
    display.show(Image.SAD)


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
