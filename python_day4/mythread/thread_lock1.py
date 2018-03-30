import threading

class Bank():
    def __init__(self):
        self.a = 1000
        self.b = 0
        self.mylock = threading.Lock()
        
    def transit(self):
        self.mylock.acquire()
        self.a -= 1
        self.b += 1
        self.mylock.release()
        
    def balance(self):
        self.mylock.acquire()
        if (self.a + self.b) != 1000:
            print("error balance")            
        self.mylock.release()


class TransitThread(threading.Thread):
    def __init__(self, bank, count):
        super().__init__()
        self.bank = bank
        self.count = count
    
    def run(self):
        for i in range(0, self.count):
            self.bank.transit()

class BalanceThread(threading.Thread):
    def __init__(self, bank, count):
        super().__init__()
        self.bank = bank
        self.count = count
    
    def run(self):
        for i in range(0, self.count):
            self.bank.balance()

b = Bank()
t1 = TransitThread(b, 1000000)
t2 = BalanceThread(b, 1000000)
t1.start()
t2.start()