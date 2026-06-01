import random
import time, gc
import jd9853
import tft_config
from machine import freq

tft = tft_config.config(1)

# Indicate the folders containing same name images. ex: bb-splash/bbb-splash-320x172.jpg 320 came from tft.width() and 172 came from tft.height() so you can reuse in another screen
IMAGES = ("bbb-splash", "bigbuckbunny", "Espressif_Black_Horizontal", "evil-frank", "its-a-trap", "logo", "Micropython", "rinkysplash", "rodents", "ws")

def main():

    tft.init()
    tft.fill(jd9853.BLACK)
    while True:
        for image in IMAGES:
            filename = f"{image}/{image}-{tft.width()}x{tft.height()}.jpg"
            tft.jpg(filename, 0, 0)  # Draw full screen jpg
            gc.collect()
            time.sleep(0.25)  # Wait 0.25 second

main()
# END CODE
