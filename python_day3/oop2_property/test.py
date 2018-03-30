from oop import House
from oop import HouseManager

house_manager = HouseManager.HouseManager()
h = House.House(100, 'asdfasf')
house_manager.add(h)
h = House.House(200, 'sdfsdfasf')
house_manager.add(h)
house_manager.print_all()
print(house_manager.add(h))