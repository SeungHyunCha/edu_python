from socket import *

ip = '127.0.0.1'
port = 62500
address = (ip, port)
mysock = socket(AF_INET, SOCK_STREAM)
mysock.connect(address)

data = mysock.recv(1024)
print(data.decode('utf-8'))

data = mysock.recv(1024)
print(data.decode('utf-8'))

mysock.close()