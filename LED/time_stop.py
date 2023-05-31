from machine import Pin, Timer
import time

led_25 = Pin(25,Pin.OUT)
led_14 = Pin(14,Pin.OUT)
#led_15 = Pin(15,Pin.OUT)
tin = Timer()


def tick(tim):
 led_25.toggle()
    

while True:
    led_14.toggle()
    time.sleep(1)
    y=0
