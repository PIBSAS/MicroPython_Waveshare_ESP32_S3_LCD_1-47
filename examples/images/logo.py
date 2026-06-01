"""
logo.py

    Draw different sized png MicroPython logos to test the png decoder and clipping. 
    Copy the png logo files to the same directory as this file.

    The MicroPython logo is copyright George Robotics Ltd.
"""

import gc
from time import sleep, ticks_ms
import jd9853
import tft_config

LOGOS = (
    (64, 64),
    (128, 128),
    (240, 240),
    (80, 160),
    (160, 80),
    (128, 160),
    (160, 128),
    (135, 240),
    (240, 135),
    (172, 320),
    (320, 172),
    (240, 320),
    (320, 240),
    (320, 480),
    (480, 320)
)

#name = "evil-frank"
name = "bbb-splash"
#name = "bigbuckbunny"
#name = "its-a-trap"
#name = "logo"
#name = "Micropython"
#name = "rinkysplash"
#name = "rodents"
#name = "ws"
#name = "Espressif_Black_Horizontal"
#name = "Espressif_Black_Vertical"
#name = "Espressif_White_Horizontal"
#name = "Espressif_White_Vertical"
#name = "Espressif_Stadar_Vertical"
gc.collect()
tft = tft_config.config(0, buffer_size=32768)

def main():
    '''
    Decode and draw png on display
    '''

    tft.init()

    for width, height in LOGOS:
        tft.fill(jd9853.WHITE)
        filename = f"{name}/{name}-{width}x{height}.png"
        start = ticks_ms()
        tft.png(filename, 0, 0)
        gc.collect()
        print(f"Displaying {filename} took "
              f"{ticks_ms()-start}ms"
        )
        sleep(2)
main()
