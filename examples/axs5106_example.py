from machine import I2C, Pin
from axs5106 import AXS5106

i2c = I2C(0, scl=Pin(41), sda=Pin(42))

touch = AXS5106(i2c, width=320, height=1720)

while True:
    t = touch.touches()
    if t:
        print(t)