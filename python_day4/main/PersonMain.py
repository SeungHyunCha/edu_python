from main import person

class PersonManager(object):
    def __init__(self):
        self.filename = "plist.data"  
        self.plist = []
        self.load_data()
    
    def load_data(self):
        try:
            f = open(self.filename, "rb")
            import pickle
            self.plist = pickle.load(f)
            f.close()
            print("prev data loading")
        except FileNotFoundError:
            print("No prev data")
            
    def add(self, p):
        return self.plist.append(p)
        self.save_data()
        
    def print_all(self):
        for stu in self.plist:
            print(stu.show_info())
    
    def save_data(self):
        f = open(self.filename, "wb")
        import pickle
        pickle.dump(self.plist, f)
  
    def find(self, name):
        for p in self.plist:
            if p.name == name:
                print(p.show_info())

    def count(self):
        print(len(self.plist))
    
p = person.Student("cha", 1102)
mgr = PersonManager()
mgr.add(p)
p = person.Student("lee", 2202)
mgr.add(p)
# mgr.count()
# p = mgr.find("cha")
t = person.Teacher("pack", "math", 101234)
mgr.add(t)

mgr.print_all()


