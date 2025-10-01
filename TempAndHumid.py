from machine import Pin
import dht
from time import sleep

DHT_PIN = 22
sensor = dht.DHT11(Pin(DHT_PIN))

while True:
    try:
        # 1. Measure the data (this initiates the communication)
        sensor.measure()
        
        # 2. Read temperature in Celsius and humidity
        temp_celsius = sensor.temperature()
        humidity = sensor.humidity()
        
        # 3. Calculate Fahrenheit
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        
        # 4. Print the results
        print("-" * 25)
        print(f"Temperature: {temp_celsius:.1f} °C / {temp_fahrenheit:.1f} °F")
        print(f"Humidity:    {humidity:.1f} %")
            
    except OSError as e:
        # The DHT sensors are sensitive to timing; errors are common.
        print("Failed to read sensor. Retrying...")
        
    sleep(3) # The DHT11 is slow and should only be read every 2-3 seconds