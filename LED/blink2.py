import machine
import random
from time import sleep

# Initialize pins
pin_led = machine.Pin(25, machine.Pin.OUT)
pin_led1 = machine.Pin(14, machine.Pin.OUT)
pin_led2 = machine.Pin(15, machine.Pin.OUT)

# Turn off all pins initially
pin_t = [pin_led, pin_led1, pin_led2]
while True:
# Loop 10 times
    for _ in range(10):        # Randomly select a pin to blink
        pin = random.choice(pin_t)
        
        # Generate random sleep duration between 0.1 and 0.5 seconds
        blink_duration = random.uniform(0.1, 0.5)
        
        # Toggle the selected LED pin
        pin.on()
        
        # Wait for the random blink duration
        sleep(blink_duration)
        
        pin.off()
        
        # Generate random sleep duration between 0.1 and 0.5 seconds
        wait_duration = random.uniform(0.1, 0.5)
        
        # Wait for the random wait duration before next blink
        sleep(wait_duration)
        
    break

