from machine import Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd

isMotion = False

PIR_PIN = 14
LED_PIN = 12
I2C_ADDR = 0x27 
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()

# GND, Sig, VCC
# You MUST add a pin arg
def handleMotion(pin):
    global isMotion
    isMotion = True

led = Pin(LED_PIN, Pin.OUT)
PIR = Pin(PIR_PIN, Pin.IN)
PIR.irq(trigger = Pin.IRQ_RISING, handler = handleMotion)

while True:
    if isMotion:
        led.value(True)
        print("Motion")
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Di Chuyen")
        sleep(4)
        led.value(False)
        print("No Motion")
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Khong di chuyen")
        isMotion = False
   
""" also works
while True:
    if PIR.value() == 1:  # Motion detected
        led.value(True)
        print("Motion detected")
    else:
        led.value(False)
        print("No motion")
    sleep(0.1)  # adjust refresh rate
"""

        

