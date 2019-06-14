from microbit import *
import radio

radio.on()
radio.config(channel = 23)
while True:
  if button_a.was_pressed():
    radio.send("left")
    display.show(Image.ARROW_N)
    sleep(300)
    display.clear()
  elif button_b.was_pressed():
    radio.send("right")
    display.show(Image.ARROW_S)
    sleep(300)
    display.clear()