"""Waveshare ESP32-S3-Touch-LCD-1.47"""

from machine import Pin, SPI
import jd9853
TFA = 0
BFA = 0

Pin(46, Pin.OUT).value(1)

def config(rotation=0, buffer_size=0, options=0):

    return jd9853.JD9853(
        SPI(
            1,
            baudrate=40000000,
            sck=Pin(38),
            mosi=Pin(39),
        ),
        172,
        320,
        reset=Pin(40, Pin.OUT),
        cs=Pin(21, Pin.OUT),
        dc=Pin(45, Pin.OUT),
        backlight=Pin(46, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )
