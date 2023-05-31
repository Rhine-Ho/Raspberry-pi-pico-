import time, math
from machine import Pin

trig = Pin(10,Pin.OUT)
echo = Pin(4,Pin.IN,Pin.PULL_DOWN)

def ping():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count=0
    timeout=False
    
    while not echo.value():
        time.sleep_us(10)
        count += 1
        if count > 10000:
            timeout=True
            Break
            
            if timeout:
                duration=0
            else:
                count=0
                start=time.ticks_us()
                while echo.value():
                    time.sleep_us(10)
                    count+=1
                    
                if count>2320:
                    break
                duration=time.ticks_diff(time.ticks_us(),start)
            return duration
        
        while True:
            distance=round(ping()/58)
            print("%scm"%distance)