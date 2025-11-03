import network
import time
import gc

try: import usocket as socket
except: import socket as socket

def web():
    html = """
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Đây là website của ESP-32</h1>
        </body>
    </html>
    """
    return html

wifiStation = {
        "ssid" : "ESP-32 Web Server",
        "pwd" : "012345678",
}

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=wifiStation["ssid"], password=wifiStation["pwd"], authmode = network.AUTH_WPA_PSK)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

header = {
    'HTTP/1.1 200 OK\n Content-Type: text/html\nConnection: close\n\n'
}

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    conn.send(header)
    conn.sendall(web())
    conn.close
    

