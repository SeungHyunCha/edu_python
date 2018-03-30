class House:
    def __init__(self, price, address):
        self.price = price
        self.address = address
        
    def change_price(self, price):
        self.price = price
    
    def show_info(self):
#         return self.__dict__
        s = 'price=%s, address=%s' %(self.price, self.address)
        return s
    
