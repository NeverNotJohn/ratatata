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

spi = SPI(1, baudrate=20000000, polarity=0, phase=0, miso=None)
tft=TFT(spi,12,13,14)
tft.initr()
tft.rgb(True)


# Interrupts

def bonk():
    
    #if (sensor.value() == 0):
    #    return
    
   # Prevent all other interrupts
    if (s0.value() == 0 and s1.value() == 0 and s2.value() == 0):
        return 
        
    print("reading...")
    # Loading...
    sleep(5)
    
    if (s0.value() == 0 and s1.value() == 0 and s2.value() == 1):
        print("person 1 played")
    elif (s0.value() == 0 and s1.value() == 1 and s2.value() == 0):
        print("person 2 played")
    elif (s0.value() == 0 and s1.value() == 1 and s2.value() == 1):
        print("person 3 played")
    elif (s0.value() == 1 and s1.value() == 0 and s2.value() == 0):
        print("person 4 played")
    elif (s0.value() == 1 and s1.value() == 0 and s2.value() == 1):
        print("person 5 played")
    elif (s0.value() == 1 and s1.value() == 1 and s2.value() == 0):
        print("person 6 played")
    elif (s0.value() == 1 and s1.value() == 1 and s2.value() == 1):
        print("person 7 played")
    else:
        print("try again bitch")
        
    # Wait until the sensor is clear
    while (s0.value() != 0 or s1.value() != 0 or s2.value() != 0):
        pass
        
    print("Polaroid out!")
    
    
    

# Interrupt handling
#s0.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 0 interrupt
#s1.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 1 interrupt
#s2.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 2 interrupt


print("Begin!")

# main
while True:
    # Do idle animation
    sleep(0.5)
    bonk()
    print("Idle!")
    #led.value(0)
    #if sensor.value() == 1:
        #led.value(1)
       


