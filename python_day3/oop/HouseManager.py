class HouseManager:
    def __init__(self):
        self.house_list = []
    
    def add(self, h):
        self.house_list.append(h)
        return h

    def print_all(self):
        print("***** printall *****")
        print("length:", len(self.house_list))
        for h in self.house_list:
            print(">>", h.show_info())