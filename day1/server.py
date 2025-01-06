#!/usr/local/bin/python
#Servidor utilizando a biblioteca socket

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen()

try:
    while True:
        #cliente que tentou a conexão ao servidor
        client, adress = server.accept()
        #request
        data = client.recv(5000).decode()
        print(f'{data=}')
        #response
        client.sendall(
            "HTTP/1.0 200 OK \r\n\r\n<html><body>Hello</body></html>\r\n\r\n".encode()
        )
        client.shutdown(socket.SHUT_WR)

except Exception:
    server.close()