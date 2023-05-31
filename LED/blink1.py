import machine
import random
from time import sleep

# Initialize pins
pin_led = machine.Pin(25, machine.Pin.OUT)
pin_led1 = machine.Pin(14, machine.Pin.OUT)
pin_led2 = machine.Pin(15, machine.Pin.OUT)

# Turn off all pins initially
pin_led.off()
pin_led1.off()
pin_led2.off()

# Loop 10 times
for _ in range(10):
    # Generate random sleep duration between 0.1 and 0.5 seconds
    blink_duration = random.uniform(0.1, 0.5)
    
    # Toggle the LED pins
    pin_led.on()
    pin_led1.on()
    pin_led2.on()
    
    # Wait for the random blink duration
    sleep(blink_duration)
    
    pin_led.off()
    pin_led1.off()
    pin_led2.off()
    
    # Generate random sleep duration between 0.1 and 0.5 seconds
    wait_duration = random.uniform(0.1, 0.5)
    
    # Wait for the random wait duration before next blink
    sleep(wait_duration)
