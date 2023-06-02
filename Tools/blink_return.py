from machine import Pin,Timer
from time import sleep

button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
led0 = machine.Pin(25, machine.Pin.OUT)
led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(15, machine.Pin.OUT)
leds= [led0,led1,led2]
sw = False
memo = False
tim = Timer() # 構建定時器

def switch(tim):
    global sw ,memo
    if (button.value() == 0)  and (memo == False):
        sw = not sw
        memo = True
        sleep(0.01)
    elif (button.value() == 1):
        memo = False
        sleep(0.01)
        
    

tim.init(period=200, mode=Timer.PERIODIC, callback=switch)

while True:
    if sw == False:
        for i in range (0,3):
            print('led_a',i)
            leds[i].on()
            sleep(0.5)
            leds[i].off()
    else:
        for i in range (2,-1,-1):
            print('led_b',i)
            leds[i].on()
            sleep(0.5)
            leds[i].off()