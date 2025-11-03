try:
    import usocket as socket   
except:
    import socket              

import network                 
import esp
esp.osdebug(None)

import gc                      
gc.collect()

ssid = 'Minh Trí'           
password = '0783548752'   

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while sta.isconnected() == False:
    pass

print('Connected.')
print(sta.ifconfig())
