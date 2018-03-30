import random
from socket import *
import threading

def number_read_thread(client, com_num):
    while True:
        print("connect ...")
        user_num = client.recv(1024)
        user_num = user_num.decode('utf-8')
        user_num = int(user_num)
        
        msg = ''
        if com_num == user_num:
            msg = 'Good!'
        elif com_num < user_num:
            msg = 'please down'
        else:
            msg = 'please up'
    
        client.send(bytes(msg, 'utf-8'))
        if com_num == user_num:
            break
    client.close()

ip = '127.0.0.1'
port = 62500
address = (ip, port)
server = socket(AF_INET, SOCK_STREAM)
server.bind(address)
server.listen()

while True:
    print("waiting for connection ...")
    client, addr = server.accept()
    com_num = random.randint(1, 100)
    t1 = threading.Thread(target = number_read_thread, args=(client, com_num))
    t1.start()
    
server.close()