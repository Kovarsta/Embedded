from machine import Pin, PWM
from time import sleep

LED_PIN = 27
FREQUENCY = 1000

led = PWM(Pin(LED_PIN), FREQUENCY)

while True:
    for duty in range(0, 1024):
        led.duty(duty)
        sleep(.005)
        
    for duty in range(1023, -1):
        led.duty(duty)
        sleep(.005)   