try:
    import usocket as socket
except:
    import socket

import network
import gc
gc.collect()

ssid = 'ESP-32'
password = '012345678'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected()== False:
    pass

print('Kết nối thành công!')
print('Cấu hình mạng:', sta.ifconfig())


