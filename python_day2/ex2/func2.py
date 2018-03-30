def gugudan(start=2, end=9):
    print(start,'*', end,'=',start*end)
'''    
for i in range(2,10):
    for j in range(1,10):
        gugudan(i, j)
   '''
    
gugudan(3)     
gugudan(1, end=3)     

def mysum(*nums):
    total = 0
    print(nums)
    for i in nums:
        total += i
    return total

def mysum1(nums):
    total = 0
    print(nums)
    for i in nums:
        total += i
    return total

result = mysum(1,3,5)
print(result)
result1 = mysum(1,3,5)
print(result1)

def mydict( ** dic ):
    print(locals())
    print("keys:", dic.keys())
    print("values:", dic.values())
    
mydict(a=10, b=20)

def compfn(a, *args, **dicts):
    print(a,args,dicts)
    
compfn(3,4,5,x=3,y=4)

def getNameResult():
    return 5,3,2,0

print(getNameResult())
a,b,c,d = getNameResult()
print(a,b,c,d)

l = locals()
# print( l )
# for i in l.values():
#     print('%s:%s\n' % (i,l[i]))
    
print (dir(__builtins__))