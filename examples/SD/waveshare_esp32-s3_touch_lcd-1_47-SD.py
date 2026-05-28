"""
Waveshare ESP32-S3 Touch LCD 1.47 has SDMMC/SDIO Slot of 4 bit
SD_D2 GPIO13
SD_D3 GPIO14
SD_CMD GPIO15
SD_CLK GPIO16
SD_D0 GPIO17
SD_D1 GPIO18
"""
from machine import SDCard
import os

SD_CMD=15
SD_D0=17
SD_D1=18
SD_D2=13
SD_D3=14
SD_CLK=16

sd = SDCard(slot=1, width=4, cmd=SD_CMD, data=(SD_D0, SD_D1, SD_D2, SD_D3), sck=SD_CLK, freq=20000000)

os.mount(sd, "/sd")

print(os.listdir("/sd"))
