import machine
import utime
import _thread

internal_led = machine.Pin(25, machine.Pin.OUT)
ext_led = machine.Pin(15, machine.Pin.OUT)


def coreO_thread():
    while True:
        print("coreO")
        ext_led.toggle()
        utime.sleep(0.5)
        
_thread.start_new_thread(coreO_thread, ())
        
while True:
    print("core1")
    internal_led.toggle()
    utime.sleep(1)