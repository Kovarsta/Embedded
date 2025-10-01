from machine import Pin
from time import sleep

LED_PIN = 2
led = Pin(LED_PIN, Pin.OUT)

while True:
    led.value(True)
    sleep(1)