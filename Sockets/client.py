import socket

HOST = '192.168.0.222'
PORT =  6999

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))

socket.send("Hello World!".encode('ascii'))

print(socket.recv(1024))

