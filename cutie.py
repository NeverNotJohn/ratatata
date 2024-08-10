# Hello world!

from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math

"""
Pinout TFT Display:

LED   -> 3v3
SCK   -> 10
SDA   -> 11
A0    -> 9
RESET -> 12
CS    -> 13
GND   -> gee I wonder
VCC   -> 3v3

"""

spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=None)
tft=TFT(spi,9,12,13)
tft.initr()
tft.rgb(True)

tft.rotation(3)

def startUp():
    tft.fill(TFT.BLACK)
    tft.text((0,0), "Hello World!", TFT.WHITE, sysfont, 1)
    
# main:

startUp()
print("Done!")