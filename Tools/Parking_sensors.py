from machine import Pin, PWM
import time

# Pin connections
echo_pin = Pin(4, Pin.IN)
trig_pin = Pin(10, Pin.OUT)
buzzer_pin = Pin(28, Pin.OUT)
buzzer = PWM(buzzer_pin)

def measure_distance():
    # Generate trigger pulse
    trig_pin.off()
    time.sleep_us(2)
    trig_pin.on()
    time.sleep_us(10)
    trig_pin.off()
    
    # Measure echo pulse duration
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()
    
    pulse_duration = pulse_end - pulse_start
    
    # Convert pulse duration to distance in centimeters
    distance = pulse_duration / 58.0
    
    return distance

def sound_buzzer():
    # Generate sound on the buzzer
    buzzer.freq(100)  # Set frequency
    buzzer.duty_u16(32768)  # Set duty cycle
    time.sleep(0.5)
    buzzer.duty_u16(0)  # Stop sound
    time.sleep(0.1)

# Main loop
while True:
    distance = measure_distance()
    
    if distance < 30:  # Adjust this threshold according to your needs
        sound_buzzer()
        time.sleep(0.1)
    else:
        sound_buzzer()
        time.sleep(0.4)
