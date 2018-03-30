
import threading
import time

class Client_thread:
    def __init__(self, clientname, sec):
        self.clientname = clientname
        self.sec = sec
            
    def __call__(self):
        while True:
            print("%s - delay %s" % (self.clientname, self.sec))
            time.sleep(self.sec)
        
clientA = threading.Thread(target= Client_thread("clientA", 0.1))
clientB = threading.Thread(target= Client_thread("clientB", 0.1))

clientA.start()
clientB.start()
