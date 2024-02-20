"""
IQS5XX library example

Copy this file to the root of your CIRCUITPY drive and copy iqs5xx.py into
lib/iqs5xx/iqs5xx.py
"""
import board
from iqs5xx.iqs5xx import IQS5XX
from time import sleep


trackpad = IQS5XX(ready_pin=board.MOSI)

while True:
    try:
        x = trackpad.absolute_x
        y = trackpad.absolute_y
        if g := trackpad.get_gesture():
            print(g)
        if x != 0xFFFF and y != 0xFFFF:
            print(f'({x},{y})')
    except KeyboardInterrupt:
        break
    else:
        sleep(0.1)
