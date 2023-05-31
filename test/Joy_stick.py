import machine
import time
import math

j_x = machine.ADC(2)
j_y = machine.ADC(0)

while True:
    
    read_x = j_x.read_u16()
    read_y = j_y.read_u16()
    
    print('{}{:5}{}{:5}'.format('X = ',read_x,'Y = ',read_y))
    time.sleep(0.1)
    
