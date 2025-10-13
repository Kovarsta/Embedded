from time import sleep
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27
i2c = I2C(scl=Pin(22),sda=Pin(21), freq=100000)
lcd  = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16) # Y, X
lcd.putstr("Hello, world")