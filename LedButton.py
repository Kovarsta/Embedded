from machine import Pin
from time import sleep

LED_PIN = 27
BUTTON_PIN = 34

led = Pin(LED_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        print("Button pressed!")
        led.value(True)
        sleep(.2) # Debounce
        
    sleep(.01)