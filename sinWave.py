from machine import Pin, I2C
import time
from math import sin, cos, tan
import ssd1306

# Initialize I2C (GPIO22 = SCL, GPIO21 = SDA on ESP32)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Scan for devices
print('I2C devices found:', i2c.scan())

# Create OLED object (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear and write text
oled.fill(0)  # clear screen
amplify = 30
offset = 32    
t = 0          

while True:
    t = time.ticks_ms()*0.005
    oled.fill(0)  # clear screen each frame

    for x in range(0, 128):
        y = int(amplify * sin(0.1 * x + t) + offset)
        y2 = int(amplify * cos(0.1 * x/2*5 + t) + offset)
        y3 = int(amplify * tan(0.1 * x + t) + offset)
        if 0 <= y < 64:   # keep it in display bounds (assuming 128x64 OLED)
            oled.pixel(x, y, 1)
            oled.pixel(y2, x, 1)
            oled.pixel(y2+64, x, 1)
            oled.pixel(y2+32, x, 1)
            oled.pixel(x, y3, 1)

    oled.show()
    time.sleep(0.03)

