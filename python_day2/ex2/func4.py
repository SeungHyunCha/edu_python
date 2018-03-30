def make_calc():
    sum = 0 
    
    def add(num):   # to operate local variable
        nonlocal sum
        sum += num
    
    def total():
        return sum

    return { 'add' : add, 'total' : total }

calc = make_calc()
calc['add'](3)
calc['add'](4)
print('total', calc['total']())