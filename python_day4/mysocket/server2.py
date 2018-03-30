import random
from socket import *

sayings = '''asdfnwebfjkwefjkw
sdhjklfzxcvljwkefl
cnmvwklejwklerjkwle
sdifouwpeofjsdklfjls
asndvmnwoejwe
sdjfklsjfiowejfiow
nvmkasdfkljwlkef
dsjiowjefioanskldf
icovujiowejfklwnef
djfklsdnflkwneifojwioe
nzxmcvnjskdfhwjoefj

'''

s_list = sayings.split('\n')

def choice():
    return random.randint(0, len(s_list))

ip = '127.0.0.1'
port = 62500
address = (ip, port)
server = socket(AF_INET, SOCK_STREAM)
server.bind(address)
server.listen()

while True:
    print("waiting for connection ...")
    client, addr = server.accept()
    print("connect ...")
    client.send(b"Hello, this is Server!")
    client.send(bytes(s_list[choice()], 'utf-8'))
    client.close()
server.close()