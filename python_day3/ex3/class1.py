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

class HouseManager:
    def __init__(self):
        self.house_list = []
    
    def add(self, h):
        self.house_list.append(h)

    def print_all(self):
        print("***** printall *****")
        print("length:", len(self.house_list))
        for h in self.house_list:
            print(">>", h.show_info())
    
    
    

    
        
house_manager = HouseManager()
h = House(100, 'asdfasf')
house_manager.add(h)
h = House(200, 'sdfsdfasf')
house_manager.add(h)
house_manager.print_all()
# h = house_manager.find(price=200)
# if h == None:
#     print("Not exist")
# else:
#     print("exist!", h.show_info())
# house_manager.remove(price=200)
# 
# if __name__ == '__main__':
#     h = House(100, 'asdfasf')
#     h.change_price(200)
#     print (h.show_info())
#     
#     house_list = []
#     h = House(100, 'asdfasf')
#     house_list.append(h)
#     h2 = House(100, 'asdfasf')
#     house_list.append(h2)
#     print( len(house_list) )