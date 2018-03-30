
myfn = lambda x: x**2

print(myfn(9))

mylist = [3,4,5,6,1,2,7,8,9]
# mylist.sort()
mylist.sort(key=lambda x:x)
print(mylist)
mylist.sort(key=lambda x:-x)
print(mylist)