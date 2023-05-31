#以掃描按鍵的方式控制LED旋轉方向
import machine
from time import sleep

button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
led0 = machine.Pin(25, machine.Pin.OUT)
led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(15, machine.Pin.OUT)
leds= [led0,led1,led2]
sw = False

def switch():
    global sw
    while (not button.value()):
        sleep(0.1)
    sw = not sw
    print(sw)

while True:
    if sw == False:
        for i in range (0,3):
            if button.value()==0:
                switch()
            print('led_a',i)
            leds[i].on()
            sleep(0.5)
            leds[i].off()
    else:
        for i in range (2,-1,-1):
            if button.value()==0:
                switch()
            print('led_b',i)
            leds[i].on()
            sleep(0.5)
            leds[i].off()