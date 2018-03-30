

mylist = []
print(dir((mylist)))
myappend = getattr(mylist, 'append')
myappend(100)
myappend(200)
print(mylist)
