from machine import Pin
from time import sleep

BUTTON_PIN = 2
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        print("Button is being pressed!")
        
    sleep(.01)
