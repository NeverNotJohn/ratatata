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
A0    -> 12
RESET -> 13
CS    -> 14
GND   -> gee I wonder
VCC   -> 3v3

button -> 2
speaker -> 3

"""

spi = SPI(1, baudrate=20000000, polarity=0, phase=0, miso=None)
tft=TFT(spi,12,13,14)
tft.initr()
tft.rgb(True)

sensor = HCSR04(trigger_pin=26, echo_pin=15, echo_timeout_us=10000)
tft.rotation(3)

# Pin Layout:

button = Pin(2, Pin.IN, Pin.PULL_DOWN)
speaker = Pin(3, Pin.OUT)

def startUp():
    
    print('Start!')
    
    tft.fill(TFT.BLACK)
    
    while True:
        
        tft.text((5,54), "Scanning...", TFT.WHITE, sysfont, 2)
        time.sleep(1)
        
        if (sensor.distance_cm() < 10):
            object_detected()
        
        tft.fill(TFT.BLACK)
        tft.text((5,54), "Scanning . . . ", TFT.WHITE, sysfont, 2)
        time.sleep(1)
        
        if (sensor.distance_cm() < 10):
            object_detected()
        
        tft.fill(TFT.BLACK)

def object_detected():
    tft.fill(TFT.BLACK)
    while sensor.distance_cm() < 10:
        tft.text((45,50), "Object", TFT.WHITE, sysfont, 2)
        tft.text((35,70), "Detected!", TFT.WHITE, sysfont, 2)
        
def beep():
    speaker.value(1)
    time.sleep(0.1)
    speaker.value(0)
    time.sleep(0.1)
    speaker.value(1)
    time.sleep(0.1)
    speaker.value(0)
    time.sleep(0.1)

        
def analyzing(pin):
    if (sensor.distance_cm() < 10):
        tft.fill(TFT.BLACK)
        tft.text((15,54), "Analyzing.", TFT.WHITE, sysfont, 2)
        beep()
        time.sleep(0.5)
        tft.text((15,54), "Analyzing..", TFT.WHITE, sysfont, 2)
        beep()
        time.sleep(0.5)
        tft.text((15,54), "Analyzing...", TFT.WHITE, sysfont, 2)
        beep()
        time.sleep(0.5)
        tft.fill(TFT.BLACK)
        tft.text((55,45), "Cutie", TFT.WHITE, sysfont, 2)
        tft.text((40,65), "Detected", TFT.WHITE, sysfont, 2)
        tft.text((70,85), "<3", TFT.WHITE, sysfont, 2)
        speaker.value(1)
        time.sleep(1)
        speaker.value(0)
        time.sleep(2)
        tft.fill(TFT.BLACK)
  
# Interrupt handling

button.irq(trigger=Pin.IRQ_RISING, handler=analyzing)  

# main:

startUp()
print("Done!")