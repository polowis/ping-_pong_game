from microbit import *
import radio

radio.on()
radio.config(channel = 23)
while True:
  x = accelerometer.get_x()
  y = accelerometer.get_y()
  z = accelerometer.get_z()
  if y <= (1800):
    radio.send("left")
    display.show(Image.ARROW_N)
    sleep(100)
    display.clear()
  elif y >= (1000):
    radio.send("right")
    display.show(Image.ARROW_S)
    sleep(100)
    display.clear()