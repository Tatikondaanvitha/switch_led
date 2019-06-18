
import RPi.GPIO as gpio
import time
gpio.setwarnings (False)
gpio.setmode (gpio.BCM)
gpio.setup(7,gpio.IN)
gpio.setup(23,gpio.OUT)

while True:
    switch = gpio.input(7)

    if (switch == 0):
        gpio.output(23,1)
        print ("led is on")

    else:
        gpio.output(23,0)
        print ("led is off")
    time.sleep(1)

    
