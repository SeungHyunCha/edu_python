

class Account:
    def __init__(self, money):
        self.money = money
    
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money
    
    def show_account(self):
        print('account=', self.money)
    
    
class YellowAccount(Account):
    def __init__(self, money, name):
        super().__init__(money)
        self.name = name
        
    def deposit(self, money):
        self.money += money*1.07

    def withdraw(self, money):
        self.money -= money + 10

    def show_account(self):
        super().show_account()
        print("account owner:", self.name)

    def __add__(self, other):
        self.money += other
        
a = YellowAccount(100, 'cha')
a.deposit(200)
a.withdraw(20)
a.show_account()

a + 100
a.show_account()
