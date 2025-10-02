from machine import Pin
from time import sleep

LED_PIN = 27
BUTTON_PIN = 34
BUTTON_FLAG = False

led = Pin(LED_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

def handleButtonInterrupt():
    global BUTTON_FLAG
    BUTTON_FLAG = not BUTTON_FLAG

button.irq(trigger = Pin.IRQ_RISING,handler = handleButtonInterrupt)

while True:
    if BUTTON_FLAG:
        print("Button pressed!")
        led.value(True)
    else:
        led.value(False)
    sleep(.01)
