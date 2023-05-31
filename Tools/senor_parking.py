from machine import Pin, PWM
import time

# Pin connections
echo_pin = Pin(4, Pin.IN)
trig_pin = Pin(10, Pin.OUT)
servo_pin = Pin(21, Pin.OUT)
servo = PWM(servo_pin)

# Sonar measurement function
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

# Fence control function
def move_fence(position):
    # Map the desired position to servo duty cycle values
    duty_cycle = int((position / 180) * 65024 + 16384)
    servo.duty_u16(duty_cycle)

# Main loop
while True:
    # Measure distance
    distance = measure_distance()
    
    # Adjust the fence position based on distance
    if distance < 50:  # Adjust this threshold according to your needs
        move_fence(90)  # Move fence to open position
    else:
        move_fence(0)  # Move fence to closed position
    
    time.sleep(0.1)  # Delay between measurements
