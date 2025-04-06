# main.py
import pyb
import time  

# LED sequence for list
led_sequence = [1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4]

for led in led_sequence:
    pyb.LED(led).on()  # Turn ON the LED
    time.sleep(1)  # Wait 1 second
    pyb.LED(led).off()  # Turn OFF the LED
