import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

Host = '192.168.0.222'
Port = 9090

server.bind((Host, Port))

server.listen(2)

while True:
    communication_socket, address = server.accept()
    print(f"Connection to {address}")
    message = communication_socket.recv(1024).decode('ascii')
    print(f'Message from client is {message}')
    communication_socket.send(f"Message received, thank you!".encode('ascii'))
    communication_socket.close()
    print(f"Connection with {address} has ended!")



