import datetime
import logging


def deco1(func):
    def new_func():
        print('Today', datetime.date.today())
        func()
    return new_func

def deco2(func):
    def new_func():
        print('python version 3.6.4')
        func()
    return new_func

def logging_deco(func):
    def new_func( *args, **dicts ):
        print('****** start ********')
        func( *args, **dicts )
        print('****** end ********')
    return new_func

def timer_deco(func):
    def new_func(myname=None):
        print('****** start timer ********')
        func(myname)
        print('****** end timer ********')
    return new_func

@deco1
@deco2
def print_hi():
    print('hello python')

def print_easy(myname=None):
    print('easy python', myname)

def print_easy1(*myname):
    print('easy python', myname)

#print_easy('cha')

print_hi()
print('-----------------------------------\n')
myeasy = timer_deco(print_easy)
# myeasy = logging_deco(myeasy)
myeasy('cha')
print('-----------------------------------\n')
# hi = deco2(print_easy)
# hi2 = deco1(hi)
# hi2()
# print_hi1 = deco1(deco2(print_hi))
# print_hi1 = deco1(print_hi)
# print_hi1()

myeasy1 = logging_deco(print_easy1)
myeasy1('cha',123)