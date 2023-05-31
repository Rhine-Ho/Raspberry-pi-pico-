from machine import Pin
import utime

led_14 = Pin(14,Pin.OUT)
led_15 = Pin(15,Pin.OUT)

led_14.value(0)
led_15.value(0)

button_11 = Pin(11, Pin.IN, Pin.PULL_UP)

def int_handler(pin):
    button_11.irq(handler=None)
    print("Interrupt Detected!")
    
    led_14.value(1)
    led_15.value(0)
    utime.sleep(1)
    led_14.value(0)
    button_11.irq(handler=int_handler)
    
button_11.irq(trigger=Pin.IRQ_FALLING,handler=int_handler)

while True:
    led_15.toggle()
    utime.sleep(1)
