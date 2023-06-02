from machine import Pin, PWM
from time import sleep

servo_pin = PWM(Pin(16))
servo_pin.freq(50)

j_x = machine.ADC(2)
j_y = machine.ADC(0)

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo(degrees):
    degrees = max(0, min(180, degrees))  # Clamp degrees between 0 and 180
    duty_cycle = map_range(degrees, 0, 180, 2000, 8000)
    servo_pin.duty_u16(int(duty_cycle))

while True:
    read_x = j_x.read_u16()
    read_y = j_y.read_u16()

    mapped_x = map_range(read_x, 0, 65535, 0, 180)
    mapped_y = map_range(read_y, 0, 65535, 0, 180)

    print('X = {:5}, Y = {:5}'.format(mapped_x, mapped_y))

    servo(mapped_x)  # Move servo based on mapped x value

    sleep(0.1)
