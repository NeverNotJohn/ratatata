from machine import Pin
from utime import sleep

start = Pin(0, Pin.IN, Pin.PULL_DOWN)       # Start button
led = Pin(1, Pin.OUT)                     # LED

print("Begin!")


# main
while True:
    if start.value() == 1:
        led.value(1)
        sleep(0.5)
    else:
        led.value(0)
        sleep(0.5)

print("Finished.")