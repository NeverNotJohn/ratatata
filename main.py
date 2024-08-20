from machine import Pin
from utime import sleep
from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
from time import sleep
from ST7735 import TFT,TFTColor
from machine import SPI,Pin


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

# Slideshow BMP files
def slideshow(file_array):
    # File array is a list of file names as a string
    for file in file_array:
        if (s0.value() == 0 and s1.value() == 0 and s2.value() == 0):
                break
        display(file)
        sleep(3)

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
        tft.text((5,54), "Poochie! >:D", TFT.WHITE, sysfont, 3)
        
        # Loop until sensor is out
        while (True):
            if (s0.value() == 0 and s1.value() == 0 and s2.value() == 0):
                break
            tft.fill(TFT.BLACK)
            tft.text((5,54), "Lorem Ipsum Message", TFT.WHITE, sysfont, 3)
            sleep(5)
            slideshow(["poochie.bmp", "poochie2.bmp"])
            
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
        
        
    print("Polaroid out!")
    
# Display bmp
def display(filePath):

    f=open(filePath, 'rb')
    if f.read(2) == b'BM':  #header
        dummy = f.read(8) #file size(4), creator bytes(4)
        offset = int.from_bytes(f.read(4), 'little')
        hdrsize = int.from_bytes(f.read(4), 'little')
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
            depth = int.from_bytes(f.read(2), 'little')
            if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                print("Image size:", width, "x", height)
                rowsize = (width * 3 + 3) & ~3
                if height < 0:
                    height = -height
                    flip = True
                else:
                    flip = True
                w, h = width, height
                tft._setwindowloc((0,0),(w - 1,h - 1))
                for row in range(h):
                    if flip:
                        pos = offset + (height - 1 - row) * rowsize
                    else:
                        pos = offset + row * rowsize
                    if f.tell() != pos:
                        dummy = f.seek(pos)
                    for col in range(w):
                        bgr = f.read(3)
                        tft._pushcolor(TFTColor(bgr[2],bgr[1],bgr[0]))
    spi.deinit()

# Check pins and return true/false
def checkPins(pin_array):
    if (s0.value() != pin_array[0] or s1.value() != pin_array[1] or s2.value() != pin_array[2]):
        return True
    else:
        return False
    

# Interrupt handling
s0.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 0 interrupt
s1.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 1 interrupt
s2.irq(trigger=Pin.IRQ_RISING, handler=bonk)          # Sensor 2 interrupt


print("Begin!")

# main

tft.fill(TFT.BLACK)
wait = 5

while True:
    # Do idle 3 animation
    print("Idle!")
    tft.fill(TFT.BLACK)
    tft.text((45,40), "Ur Old!", TFT.WHITE, sysfont, 2)
    tft.text((30,60), "8/31/2024", TFT.WHITE, sysfont, 2)
    tft.text((65,80), "<3", TFT.WHITE, sysfont, 2)
    sleep(wait)
    display("party.bmp")
    sleep(wait)
    display("miku.bmp")
    sleep(wait)
    display("cat.bmp")
    sleep(wait)
    display("sharkie.bmp")
    sleep(wait)
    
    # Other Animations
    # Defintely draw a cock
    # Funny Grace photos
    
    #led.value(0)
    #if sensor.value() == 1:
        #led.value(1)
       


