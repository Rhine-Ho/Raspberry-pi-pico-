import machine
from time import sleep

button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
pin_led = machine.Pin(25, machine.Pin.OUT)
pin_led1 = machine.Pin(14, machine.Pin.OUT)
pin_led2 = machine.Pin(15, machine.Pin.OUT)

pin_t = [pin_led, pin_led1, pin_led2]
while True:
    for j in range(5):
        for i in range(0,3):
            print(i)        
            pin_t[i].on()        
            sleep(0.2)
            pin_t[i].off()        
            sleep(0.2)
    for j in range(5):
        for i in range(2,-1,-1):
            print(i)        
            pin_t[i].on()        
            sleep(0.2)
            pin_t[i].off()        
            sleep(0.2)

    break


