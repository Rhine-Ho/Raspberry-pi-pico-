from machine import Pin, I2C, UART, ADC
from ssd1306 import SSD1306_I2C
import time

# Initialize Display
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)  # Fix the frequency value to 400000
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)

# Display numbers from 0 to 10
for i in range(11):
    disp = str(i)
    oled.text(disp, 10, 12)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)

# Display "IT Training"
oled.text("IT Training", 10, 12)
oled.show()
