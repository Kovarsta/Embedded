from machine import Pin, I2C
from i2c_lcd import I2cLcd
from time import sleep

# 3v, Pin layout, with the connectors on the right side is GND, VCC, SDA, SCL 

I2C_ADDR = 0x27 
i2c = I2C(0, sda=Pin(27), scl=Pin(26), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()

while True:
    # Print text
    lcd.putstr("Xin Chao")
    # Let text freeze for 1s
    sleep(1)
    # Clear text
    lcd.clear()
    # Let clear text freeze for 1s
    sleep(1)
    
    
    lcd.putstr("Hello World")
    sleep(1)
    lcd.clear()
    sleep(1)
    
