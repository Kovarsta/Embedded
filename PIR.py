from machine import Pin
from time import sleep

isMotion = False

PIR_PIN = 14
LED_PIN = 12

# GND, Sig, VCC
# You MUST add a pin arg
def handleMotion(pin):
    global isMotion
    isMotion = True

led = Pin(LED_PIN, Pin.OUT)
PIR = Pin(PIR_PIN, Pin.IN, Pin.PULL_DOWN)
PIR.irq(trigger = Pin.IRQ_RISING, handler = handleMotion)

while True:
    if isMotion:
        led.value(True)
        print("Motion")
        sleep(0.1)
        led.value(False)
        print("No Motion")
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

        