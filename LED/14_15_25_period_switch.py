from machine import Pin, Timer
import time

led_14 = Pin(14, Pin.OUT)
led_15 = Pin(15, Pin.OUT)
led_25 = Pin(25, Pin.OUT)
button = Pin(11, Pin.IN, Pin.PULL_UP)

tin_14_15 = Timer()
tin_25 = Timer()

period_14_15 = 500  # Initial period for pin 14 and pin 15 (in milliseconds)
period_25 = 300  # Initial period for pin 25 (in milliseconds)

def toggle_14_15(tim):
    led_14.toggle()
    led_15.toggle()

def toggle_25(tim):
    led_25.toggle()

def change_period(pin):
    global period_14_15, period_25

    if period_14_15 == 500:
        period_14_15 = 1000
        period_25 = 600
    else:
        period_14_15 = 500
        period_25 = 300

    tin_14_15.init(period=period_14_15, mode=Timer.PERIODIC, callback=toggle_14_15)
    tin_25.init(period=period_25, mode=Timer.PERIODIC, callback=toggle_25)

button.irq(trigger=Pin.IRQ_FALLING, handler=change_period)

tin_14_15.init(period=period_14_15, mode=Timer.PERIODIC, callback=toggle_14_15)
tin_25.init(period=period_25, mode=Timer.PERIODIC, callback=toggle_25)

while True:
    time.sleep(1)
