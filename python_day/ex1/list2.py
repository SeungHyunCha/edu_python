s1 = 'Python'
s2 = s1

print ('s1',id(s1))
print ('s2',id(s2))
s2 = 'hi'
print ('s1',id(s1))
print ('s2',id(s2))

s3 = s1.capitalize()
print ('s1',id(s1))
print ('s2',id(s2))
print ('s3',id(s3),s3)
print ('s1',id(s1),s1)

mylist1 = [1,2,3]
mylist2 = mylist1
mylist2.append(6)
print(mylist1, mylist2)

mylist = [3,4,5,1,3,8]
mylist.sort()
print(mylist)
t = tuple(mylist1)
print(t)

mytuple = (1)
print(type(mytuple),mytuple)
mytuple = (1,)
print(type(mytuple),mytuple)
print(type(mytuple[0]))
mytuple3 = t + mytuple
print(mytuple3)
print(list(mytuple3))
print(set(mytuple3))

print( ".".join(s1))
k = str(mylist)
print(type(k),k)
print(type(eval(k)),eval(k))
print (",".join([str(i) for i in mylist]))
q = ",".join([str(i) for i in mylist])
print(q)
w = q.split(',')
print(w)

def myfind():
    return (-1, 'hello')

x,y = myfind()
if __name__ == '__main__':
    pass