import machine
from time import sleep

# Initialize pins
pin_led = machine.Pin(25, machine.Pin.OUT)
pin_led1 = machine.Pin(14, machine.Pin.OUT)
pin_led2 = machine.Pin(15, machine.Pin.OUT)

# Turn off all pins initially
pin_led.off()
pin_led1.off()
pin_led2.off()

# Loop 5 times
for i in range(5):
    # Toggle the LED pins
    pin_led.on()
    pin_led1.on()
    pin_led2.on()
    
    # Wait for 1 second
    sleep(1)
    
    pin_led.off()
    pin_led1.off()
    pin_led2.off()
    
    # Wait for 1 second
    sleep(1)
