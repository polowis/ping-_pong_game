from microbit import *
radio.on()

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    if y < (600):
        radio.
        display.show(Image.HAPPY)
        sleep(1000)
        display.clear()
    else:
        display.show(Image.SAD)