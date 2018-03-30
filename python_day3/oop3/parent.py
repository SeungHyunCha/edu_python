
        


class Parent(object):
    def __init__(self, money):
        self.money = money

    def show_money(self):
        print('money=%s' % self.money)
    
    

class Child(Parent):
    pass


p = Child(50)
p.show_money()