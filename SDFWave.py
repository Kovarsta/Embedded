from machine import Pin, I2C
import time
from math import sin, sqrt
import ssd1306
import gc

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

def length(x1, y1, x2, y2):
    # Magnitute using eucliddean 
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def sdfCircle(x, y, cx, cy, radius):
    # this is the distance from the pixel to the center, minus the radius
    # result > 0: point is OUTSIDE the circle
    # result = 0: point is ON the circle edge
    # result < 0: point is INSIDE the circle
    return length(x, y, cx, cy) - radius

while True:
    oled.fill(0)  # clear screen each frame

    for x in range(0, 128):
        for y in range(0, 64):
            mag = length(x, y, 64, 32)
            wave = sin(mag * 0.4 - time.ticks_ms() * 0.02)
            distance = mag - (16 + wave) 
            #distance = sdfCircle(x, y, 64, 32, 16)
            
            # A tolerance is required because the pixel grid is an integer
            # using wave produces a weird perspective ripple, but it works, the rest of the code is still bugged though
            if abs(wave) < 0.5:
                oled.pixel(x, y, 1)
    oled.text(f"Allocated RAM: {gc.memory_alloc()}", 0, 0)
    oled.show()
    time.sleep(0.03)

