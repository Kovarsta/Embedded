from machine import Pin, I2C
from i2c_lcd import I2cLcd
import dht
from time import sleep

DHT_PIN = 19
sensor = dht.DHT11(Pin(DHT_PIN))

I2C_ADDR = 0x27 
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()

def getTempAndHumid(sensor_obj):
    sensor_obj.measure()
    temp = sensor_obj.temperature()
    humid = sensor_obj.humidity()
    
    return {
        "temp": temp,
        "humid": humid,
    }

while True:
    try:
        data = getTempAndHumid(sensor)
        temp = data["temp"]
        humid = data["humid"]        
        
        tempLabel = f"Nhiet do: {temp}C"
        humidLabel = f"Do am: {humid}%"
        
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(tempLabel)
        lcd.move_to(0, 1)
        lcd.putstr(humidLabel)
        
        print(f"Nhiet do la: {tempLabel}")
        print(f"Do am la: {humidLabel}")
    except Exception as e:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Loi DHT")
        lcd.move_to(0, 1)
        lcd.putstr("Thu lai trong 3s")
        print("Loi doc sensor")
        
    
    sleep(3)
        
    
    



