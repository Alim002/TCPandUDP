from socket import socket, SOCK_DGRAM, AF_INET

clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('localhost', 5000)
message = input('Input lowercase sentence: ')

try:
    sent = clientSocket.sendto(message.encode('utf-8'), serverAddress)

    data, server = clientSocket.recvfrom(2048)

finally:
    print('Closing socket . . . ')
    clientSocket.close()

