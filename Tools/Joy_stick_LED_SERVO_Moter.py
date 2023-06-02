from machine import Pin, ADC, PWM
from time import sleep

led_14 = Pin(14, Pin.OUT)
led_15 = Pin(15, Pin.OUT)
led_25 = Pin(25, Pin.OUT)

j_x = ADC(2)
j_y = ADC(0)

servo_pin = PWM(Pin(16))
servo_pin.freq(50)

def var():
  

    print('{}{:5}{}{:5}'.format('X = ', read_x, 'Y = ', read_y))

    if (read_x > 30000) and (read_y > 60000):
        led_14.on()
        sleep(0.1)
    elif (read_x < 1000) and (read_y < 30000):
        led_25.on()
        sleep(0.1)
    elif (read_x > 60000) and (read_y < 30000):
        led_15.on()
        sleep(0.1)
    else:
        led_14.off()
        led_15.off()
        led_25.off()
        sleep(0.1)


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

    servo(mapped_x)  # Move servo based on mapped x value

    var()
