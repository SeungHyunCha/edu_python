class Person:
    def __init__(self, name):
        self.name = name
        
    def show_info(self):
        return self.name
        
class Student(Person):
    def __init__(self, name, num):
        super().__init__(name)
        self.num = num
        
    def show_info(self):
        s = "%s, %s" % (super().show_info(), self.num)
        return s
    
class Teacher(Person):
    def __init__(self, name, subject, number):
        super().__init__(name)
        self.subject = subject
        self.number = number
        
    def show_info(self):
        s = "%s, %s, %s" % (super().show_info(), self.subject, self.number)
        return s
    
    