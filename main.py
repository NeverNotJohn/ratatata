from machine import Pin
from utime import sleep

start = Pin(0, Pin.IN, Pin.PULL_DOWN)                    # Start button
led = Pin(1, Pin.OUT)                                    # LED
s0 = Pin(2, Pin.IN, Pin.PULL_DOWN)                       # sensor 0
s1 = Pin(3, Pin.IN, Pin.PULL_DOWN)                       # sensor 1
s2 = Pin(4, Pin.IN, Pin.PULL_DOWN)                       # sensor 2
sensor = Pin(5, Pin.IN, Pin.PULL_DOWN)                   # polaroid sensor


# Interrupts

def bonk(pin):
    
    if (sensor.value() == 0):
        return
    
    if (s0.value() == 0 and s1.value() == 0 and s2.value() == 0):
        print("person 0 played")
    elif (s0.value() == 0 and s1.value() == 0 and s2.value() == 1):
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
    
    

# Interrupt handling
start.irq(trigger=Pin.IRQ_RISING, handler=bonk)       # Start button interrupt


print("Begin!")

# main
while True:
    # Do idle animation
    led.value(0)
    if sensor.value() == 1:
        led.value(1)
       


