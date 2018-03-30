def hello():
    print('hello')

hello()

print( hello )

h = hello
h()

fnlist = [h, hello]
fnlist[0]()

def hello1(myname=None):
    print('hello', myname)
    
a = hello1
a('cha')

fnlist = [a, hello1]
fnlist[0]()