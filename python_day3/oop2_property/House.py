class House:
    def __init__(self, price, address):
        self.__price = price
        self.__address = address
        
    def change_price(self, price):
        self.__price = price
    
    def show_info(self):
#         return self.__dict__
        s = 'price=%s, address=%s' %(self.__price, self.__address)
        return s
    @property
    def price(self):
        return self.__price
    @property
    def address(self):
        return self.__address
    
    @price.setter
    def price(self, price):
        self.__price = price
        
    @address.setter
    def address(self, address):
        self.__address = address
        
if __name__ == '__main__':
    h = House(100, 'asdfasf')
#     h.__price = 300
#     print(h.show_info())
#     h.change_price(400)
#     print(h.show_info())
#     print(dir(h))
#     h._House__price = 500
#     print(h.show_info())
    h.price = 200
    print ( h.price )
    print ( h.address )
    print ( h.__dict__ )
