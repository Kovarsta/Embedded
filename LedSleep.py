from machine import Pin
import time

LED_PIN = 23
SLEEP_TIME = 5
led = Pin(LED_PIN, Pin.OUT)

while True:
    led.value(True)
    print(f"LED on for {SLEEP_TIME} second(s).")
    
    time.sleep(5)
    
    led.value(False)
    print(f"LED off for {SLEEP_TIME} second(s).")
    
    time.sleep(5)