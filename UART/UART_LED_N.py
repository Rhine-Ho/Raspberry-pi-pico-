import uos
import machine
import utime

data = b""
uart0 = machine.UART(0,baudrate=115200)
led = machine.Pin(15, machine.Pin.OUT)

def sendCMD_waitResp(cmd, uart=uart0, timeout=100):
    print("CMD: " + cmd)
    uart.write(cmd)
    
def waitResp(uart=uart0, timeout=100):
    global data
    prvMills = utime.ticks_ms()
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            data = b"".join([data, uart.read(1)])           

led.off()

while True :
    waitResp()
    if data != b'' :
        print(data)
        data= str(data)
        if (data.find('on'))>=0:
            led.value(1)
            sendCMD_waitResp('LED_ON\r\n')
        elif (data.find('off'))>=0:
            led.value(0)
            sendCMD_waitResp('LED_OFF\r\n')
        data = b''
    utime.sleep(0.1)