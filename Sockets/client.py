import socket

Host = 'hostaddress'
Port =  9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))

socket.send("Hello World!".encode('ascii'))

print(socket.recv(1024))

