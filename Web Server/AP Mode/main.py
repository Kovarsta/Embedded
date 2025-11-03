import socket

def web_page():
    html = """
    HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        
        <body>
            <h1>Web Server của ESP-32</h1>
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
    response = web_page()
    conn.sendall(response)
    conn.close()
