mylist = [1,2,3,4,5]
 
for i in range(5):
    print(mylist[i])
     
it = iter(mylist)
 
print(it.__next__())
print( next(it) )
print( next(it) )
print( next(it) )
print( next(it) )
 
def my_gen():
    n=0
    while n <= 10:
        yield n # print value
        n +=1
         
a = my_gen()
print(type(a))
print(next(a))
print(next(a))
print(next(a))

def co_routine():
    total = 0
    while True:
        n = (yield)
        total += n
        print('total =', total)
    
b = co_routine()
print(next(b))
b.send(1)
b.send(9)

print(dir(b))
