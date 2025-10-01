from machine import Pin, I2C
import ssd1306

# Initialize I2C (GPIO22 = SCL, GPIO21 = SDA on ESP32)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Scan for devices
print('I2C devices found:', i2c.scan())

# Create OLED object (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear and write text
oled.fill(0)  # clear screen
oled.text("Hello ESP32!", 0, 0)
oled.text("with OLED", 0, 16)
oled.show()
