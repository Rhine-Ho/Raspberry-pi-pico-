from machine import Pin, PWM
from time import sleep

servoPin = PWM(Pin(16))
servoPin.freq(50)

def servo(degrees):
    if degrees > 360: degrees = 360
    if degrees < 0: degrees = 0
    
    maxDuty=8000
    minDuty=2000
    newDuty = minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))
     
    
while True:
    for degree in range(0,360,1):
        servo(degree)
        sleep(0.01)

