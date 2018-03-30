from socket import *

ip = '127.0.0.1'
port = 62500
address = (ip, port)
mysock = socket(AF_INET, SOCK_STREAM)
mysock.connect(address)
while True:
    print("choose 1~100")
    user_num = input('>>')
    mysock.send(bytes(user_num,'utf-8'))
    data = mysock.recv(1024)
    data = data.decode('utf-8')
    print(data)
    
    if data == 'Good!':
        break

mysock.close()
print('exit client')