from socket import *

ip = '127.0.0.1'
port = 62500
address = (ip, port)
server = socket(AF_INET, SOCK_STREAM)
server.bind(address)
server.listen()
print("socket server started..waiting")

client, addr = server.accept()
print("access client!")

client.send(b"Hello client")
print("send a message to client")

client.close()
server.close()
print("exit server")
