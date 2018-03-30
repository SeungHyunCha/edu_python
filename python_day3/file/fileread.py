flist = []

f = open('testfile.txt','r')
# t = f.read()
for line in f:
    flist.append(line.strip())
f.close()
str = '*'*50
f = open('testfile.txt','r')
tl = f.readlines()
f.close()
print(flist)
# print(t[0], t[1], t[2])
print(str)
print(tl)
print(tl[0], tl[1], tl[2])