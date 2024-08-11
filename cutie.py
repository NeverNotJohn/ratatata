# Hello world!

from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
from hcsr04 import HCSR04
from time import sleep



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

sensor = HCSR04(trigger_pin=0, echo_pin=1, echo_timeout_us=10000)

tft.rotation(3)

def startUp():
    
    print('Start!')
    
    tft.fill(TFT.BLACK)
    
    while True:
        
        tft.text((5,54), "Scanning...", TFT.WHITE, sysfont, 2)
        time.sleep(3)
        
        if (sensor.distance_cm() < 10):
            cutie_detected()
        
        tft.fill(TFT.BLACK)
        tft.text((5,54), "Scanning . . . ", TFT.WHITE, sysfont, 2)
        time.sleep(3)
        
        if (sensor.distance_cm() < 10):
            cutie_detected()
        
        tft.fill(TFT.BLACK)

def cutie_detected():
    print("Cutie Detected!")
    
# main:

startUp()
print("Done!")