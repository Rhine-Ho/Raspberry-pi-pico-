from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(28))

pwm.duty_u16(32768)

while True:
    for duty in range(500, 3000, 50):
        print(freq)
        pwm.freq(freq)
        sleep(0.1)

