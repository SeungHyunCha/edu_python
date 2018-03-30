import random
from socket import *
import threading


def broadcast(msg):
    for sock in c_list:
        sock.send(bytes(msg, 'utf-8'))


def number_read_thread(client):
    global com_num
    while True:
        print("connect ...")
        user_num = client.recv(1024)
        user_num = user_num.decode('utf-8')
        user_num = int(user_num)
        
        msg = '%s : ' % user_num
        if com_num == user_num:
            msg += 'Good!'
        elif com_num < user_num:
            msg += 'please down'
        else:
            msg += 'please up'
        
        broadcast(msg)    
        if com_num == user_num:
            com_num = random.randint(1, 100)
            print("win:%s", client)
    client.close()

ip = '127.0.0.1'
port = 62500
address = (ip, port)
server = socket(AF_INET, SOCK_STREAM)
server.bind(address)
server.listen()
c_list = []
com_num = random.randint(1, 100)
while True:
    print("waiting for connection ...")
    client, addr = server.accept()
    c_list.append(client)
    t1 = threading.Thread(target = number_read_thread, args=(client,))
    t1.start()
    
server.close()