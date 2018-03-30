def sum(a):
    total = a+1
    def inner_sum():
#         nonlocal total
#         total += 1
        print( total )
    return inner_sum

in_sum = sum(5)
in_sum()

def sum1(a):
    total = a+1
    def inner_sum():
        print( total )
    inner_sum()
    
sum1(3)

var = 0
def outter():
    var = 77
#     print(locals())
    def inner():
#         global var
        nonlocal var
        var += 1
        print(var)
        aa()
#         print(locals())
#     inner()
    def aa():
        print('aa')
    return inner

a = outter()
a()
a()

b = outter()
b()
b()