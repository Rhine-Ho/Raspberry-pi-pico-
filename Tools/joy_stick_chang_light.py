import machine
import utime

led_14 = machine.Pin(14, machine.Pin.OUT)
led_15 = machine.Pin(15, machine.Pin.OUT)
led_25 = machine.Pin(25, machine.Pin.OUT)

j_x = machine.ADC(2)
j_y = machine.ADC(0)

def var():
    read_x = j_x.read_u16()
    read_y = j_y.read_u16()
    
    print('{}{:5}{}{:5}'.format('X = ',read_x,'Y = ',read_y))

    if (read_x < 10000) and (read_y > 60000):
        led_14.on()
        utime.sleep(0.1)

    elif (read_x < 1000) and (read_y < 1000):
        led_25.on()
        utime.sleep(0.1)

    elif (read_x > 30000) and (read_y < 1000):
        led_15.on()
        utime.sleep(0.1)
    else:
        led_14.off()
        led_15.off()
        led_25.off()
        utime.sleep(0.1)


while True:
    var()