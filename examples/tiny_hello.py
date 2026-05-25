"""
hello.py

    Writes "Hello!" in random colors at random locations on the display.
"""

import random
import time
import jd9853
import tft_config
import vga1_8x8 as font

tft = tft_config.config(0)

def center(text):
    length = len(text)
    tft.text(
        font,
        text,
        tft.width() // 2 - length // 2 * font.WIDTH,
        tft.height() // 2 - font.HEIGHT,
        jd9853.WHITE,
        jd9853.RED)

def main():
    tft.init()

    tft.fill(jd9853.RED)
    center("Hello!")
    time.sleep(2)
    tft.fill(jd9853.BLACK)

    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(jd9853.BLACK)
            col_max = tft.width() - font.WIDTH*6
            row_max = tft.height() - font.HEIGHT

            for _ in range(128):
                tft.text(
                    font,
                    "Hello!",
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    jd9853.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    jd9853.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)))


main()
