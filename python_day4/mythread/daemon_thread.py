import threading
import time


def daemon_thread():
    for i in range(20):
        print('daemon %s' % i)
        time.sleep(0.1)

def user_thread():
    for i in range(6):
        print('user %s' % i)
        time.sleep(0.1)
        


t1 = threading.Thread(target = daemon_thread)
# t1.setDaemon(True)
t2 = threading.Thread(target = user_thread)

t1.start()
t2.start()