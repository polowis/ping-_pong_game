"""
@contributors: 

"""

#import all necessary modules
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
    
    #return the x and y value of the ball, 
    #private method, we don't want this to be called outside of the class.
    def __getCurrentBallPosition(self):
        return self.x, self.y
    
    #check condition of the paddle, if bottom paddle position less than 1, assign 1 to its value
    #prevents index out of bounds
    #private method
    def __getSetPaddle(self):
        if self.bottomPaddle < 1:
            self.bottomPaddle = 1
        elif self.bottomPaddle > 4:
            self.bottomPaddle = 4
    
    #the setPaddle method takes 1 parameter which is the message
    def setPaddle(self, message): #(SetPaddle) reads the message that is sent from the movement microbit and is used to move the paddle either left or right.
        if message == "right":
            self.bottomPaddle += 1
            #move the bottom paddle by one according to the message
            #the top paddle is controlled by the AI
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
        
    #control AI movement 
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
    
    #the ball movement
    def update(self):
        if self.y == 2: #start from the center of the microbit and move randomly
            self.x = self.x + self.yspeed
            self.y = self.y + self.yspeed
        elif self.y == 1 or self.y == 3: #check if the ball hit at point 1 or 3, 
            if self.y == 1: #if it does
                if self.topPaddle == self.x: #get the paddle position, if it hits the paddle
                    self.xspeed = 1 #increase xspeed and yspeed by 1
                    self.yspeed = 1
                elif self.topPaddle - 1 == self.x: #the paddle has two pixel, check if it hits the other pixel
                    self.xspeed = -1 #set xspeed to -1 and yspeed to 1, this create the different angle for the ball to be bound
                    self.yspeed = 1
            else: #check the bottom paddle, see if the ball hits the paddle
                if self.bottomPaddle == self.x:
                    self.xspeed = 1
                    self.yspeed = -1
                elif self.bottomPaddle - 1 == self.x:
                    self.xspeed = -1
                    self.yspeed = -1
            #return the result
            self.x += self.xspeed
            self.y += self.yspeed 
            
        else: #check if the ball doesnt hit the paddle
            self.x += self.xspeed
            self.y += self.yspeed
        if self.x <= 0 or self.x >= 4: #check the side of the microbit
            self.xspeed = self.xspeed * -1
        #check the top and bottom paddle, if it doesnt hit the paddle, if it hits the paddle, it will bounce back
        #if it doesnt, the y position keeps increasing. 
        #return the result
        if self.y <= 0:
            return 1
        elif self.y >= 4:
            return 2
        else:
            return 0


          
#call the class
#parameters are optional, default is x = 2, y = 2, xspeed and yspeed are at random
ball = Ball()

#create a function
def function():
     message = radio.receive() #receive the data from the radio
     ball.setPaddle(message) # pass the data to setPaddle function, with message as the parameter
     ball.AI() #activate AI
     edges = ball.update() #check the edges, see if it hits


ball.show() #display the ball at the start, default is x = 2, y = 2 which is in the middle
sleep(500) 
while True: #Main Loop
     function() #call the function
     ball.show() #display the ball after update the position
     if ball.update() != 0:
        break
        sleep(500)
#check if function update return a number, determine where the ball hits
if ball.update() == 1:
    #if the player wins, display image
    display.show(Image.HAPPY)
#if the AI wins, display image
elif ball.update() == 2:
    display.show(Image.SAD)



