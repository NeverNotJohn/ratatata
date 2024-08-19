from machine import Pin
from utime import sleep
from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
from time import sleep


start = Pin(0, Pin.IN, Pin.PULL_DOWN)                    # Start button
led = Pin(1, Pin.OUT)                                    # LED
s0 = Pin(2, Pin.IN, Pin.PULL_DOWN)                       # sensor 0
s1 = Pin(3, Pin.IN, Pin.PULL_DOWN)                       # sensor 1
s2 = Pin(4, Pin.IN, Pin.PULL_DOWN)                       # sensor 2
sensor = Pin(5, Pin.IN, Pin.PULL_DOWN)                   # polaroid sensor

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

# TFT init
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, miso=None)
tft=TFT(spi,12,13,14)
tft.initr()
tft.rgb(True)
tft.rotation(3)


# Interrupts

def bonk(pin):
    
    #if (sensor.value() == 0):
    #    return
    
   # Prevent all other interrupts
    if (s0.value() == 0 and s1.value() == 0 and s2.value() == 0):
        return 
        
    print("reading...")
    tft.fill(TFT.BLACK)
    # Loading...
    
    for i in range(3):
        tft.text((5,54), "reading.", TFT.WHITE, sysfont, 2)
        sleep(0.5)
        tft.text((5,54), "reading..", TFT.WHITE, sysfont, 2)
        sleep(0.5)
        tft.text((5,54), "reading...", TFT.WHITE, sysfont, 2)
        sleep(0.5)
        tft.fill(TFT.BLACK) # can probs make more efficient clearing only periods
    
    
    if (s0.value() == 0 and s1.value() == 0 and s2.value() == 1):
        tft.text((5,54), "person 1!", TFT.WHITE, sysfont, 2)
    elif (s0.value() == 0 and s1.value() == 1 and s2.value() == 0):
        tft.text((5,54), "person 2!", TFT.WHITE, sysfont, 2)
    elif (s0.value() == 0 and s1.value() == 1 and s2.value() == 1):
        tft.text((5,54), "person 3!", TFT.WHITE, sysfont, 2)
    elif (s0.value() == 1 and s1.value() == 0 and s2.value() == 0):
        tft.text((5,54), "person 4!", TFT.WHITE, sysfont, 2)
    elif (s0.value() == 1 and s1.value() == 0 and s2.value() == 1):
        tft.text((5,54), "person 5!", TFT.WHITE, sysfont, 2)
    elif (s0.value() == 1 and s1.value() == 1 and s2.value() == 0):
        tft.text((5,54), "person 6!", TFT.WHITE, sysfont, 2)
    elif (s0.value() == 1 and s1.value() == 1 and s2.value() == 1):
        tft.text((5,54), "person 7!", TFT.WHITE, sysfont, 2)
    else:
        tft.text((5,54), "who tf?! Invalid Input Bitch Try Again", TFT.WHITE, sysfont, 2)
        sleep(3)
        tft.fill(TFT.BLACK)
        
    # Wait until the sensor is clear
    while (s0.value() != 0 or s1.value() != 0 or s2.value() != 0):
        pass
        
    print("Polaroid out!")
    
    
    

# Interrupt handling
s0.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 0 interrupt
s1.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 1 interrupt
s2.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 2 interrupt


print("Begin!")

# main

tft.fill(TFT.BLACK)

while True:
    # Do idle 3 animation
    print("Idle!")
    tft.text((30,45), "Ur Old!", TFT.WHITE, sysfont, 2)
    tft.text((20,65), "8/31/2024", TFT.WHITE, sysfont, 2)
    tft.text((70,85), "<3", TFT.WHITE, sysfont, 2)
    sleep(5)
    tft.fill(TFT.BLACK)
    sleep(5)
    
    # Other Animations
    # Defintely draw a cock
    # Funny Grace photos
    
    #led.value(0)
    #if sensor.value() == 1:
        #led.value(1)
       


