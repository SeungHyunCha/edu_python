'''
Created on 2018. 3. 26.

@author: echaseu
'''

myname = 'cha'
print( myname )

# myname = 'cc \t a \n cha'
# print( myname )

a = '123'
b = 3
# b = 'abc'
# print( a*b )
print('---' * 10)

s = 'python'
print(s[0])
print(s[1:4])

import time
now = time.localtime()
print ( now )
print ( now.__str__() )
print ( str(now) )

a = 1
b = 2

print(eval(repr('a+b')))
print(eval(str('a+b')))
print(s.index('th'))
print(s[2])
print( '        abc          '.strip() ) 
print( '        abc      abc       aaa  '.strip() ) 
print( 'aaa abc      abc       aaa  '.strip('a') )
print('a-b-c-d-e'.split( sep = '-')) 
mylist = [1,3,5]
mylist.append(7)
mylist.append(7)
mylist.remove(1)
mylist.pop(-1)
mylist.insert(-1, 7)

print( mylist )
print( set(mylist) )

if __name__ == '__main__':
    pass