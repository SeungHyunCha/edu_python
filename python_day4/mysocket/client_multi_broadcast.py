from socket import *
import threading

ip = '127.0.0.1'
port = 62500
address = (ip, port)
mysock = socket(AF_INET, SOCK_STREAM)
mysock.connect(address)


def read_thread():
    while True:
        data = mysock.recv(1024)
        data = data.decode('utf-8')
        print(data)

t1 = threading.Thread(target= read_thread)
t1.start()

while True:
    print("choose 1~100")
    user_num = input('>>')
    mysock.send(bytes(user_num,'utf-8'))
    read_thread()

mysock.close()
print('exit client')