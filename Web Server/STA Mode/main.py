import network
import time
import gc

try: import usocket as socket
except: import socket as socket

def web():
    html = """\
    <html>
        <head>
            <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Day la website cua ESP-32</h1>
        </body>
    </html>
    """
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    conn.send('HTTP/1.1 200 OK\n Content-Type: text/html\nConnection: close\n\n')
    conn.sendall(web())
    conn.close()
    gc.collect()

