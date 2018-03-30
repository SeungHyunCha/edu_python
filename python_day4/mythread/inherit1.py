import threading
import time

class Client_thread(threading.Thread):
    def __init__(self, clientname, sec):
        super().__init__()
#         threading.Thread.__init__(self)
        self.clientname = clientname
        self.sec = sec
        
    def run(self):
        while True:
            print("%s - delay %s" % (self.clientname, self.sec))
            time.sleep(self.sec)
        
clientA = Client_thread("clientA,", 0.1)
clientB = Client_thread("clientB,", 0.1)

clientA.start()
clientB.start()