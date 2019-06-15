from microbit import *
import radio

radio.on()
radio.config(channel = 23) #The channel sends the messages directly to the Master bit without interuptions.
while True:
  x = accelerometer.get_x() #Reads the horizontal numbers
  y = accelerometer.get_y() #Reads the vertical numbers
  z = accelerometer.get_z() #Reads the movement going forward and backward
  
  if y <= (1800): #If the vertical numbers exceed this the code reads that the user is moving the glove up
    radio.send("left") #This is the message that the Master bit will receive
    display.show(Image.ARROW_W) #Shows the user that the message that was sent makes the paddle go Left
    sleep(100)
    display.clear()
    
  elif y >= (1000): #If the vertical numbers become lower then this number the code will read this as the user is moving the glove down
    radio.send("right") #This is the message that the Master bit will receive
    display.show(Image.ARROW_E) #Shows the user that the message that was sent makes the paddle go Right
    sleep(100)
    display.clear()
