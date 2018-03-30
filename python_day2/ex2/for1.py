for i in range(2,10):
    for j in range(1,10):
        print(i, '*', j, '=', i*j)

numlist = [ x for x in range(1,10) if x%2 == 0]
print(numlist)

numlist = [ '%s' % x if x%2 ==0 else print('') for x in range(1,10) ]
print(numlist)

for i in [ '%s' % x if x%2 ==0 else print('') for x in range(1,10) ]:
    print(i)
    
count = 3
while count:
    print(count)
    count -= 1 # do not exist ++, --