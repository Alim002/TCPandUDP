from socket import socket, SOCK_DGRAM, AF_INET

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', 5000))
print("waiting for connections")
while True:
    message, address = serverSocket.recvfrom(2048)
    print(message, address)
    message = message.upper()
    serverSocket.sendto(message, address)
serverSocket.close()
