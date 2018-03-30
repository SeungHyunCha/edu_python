mydict = {'1':'egg', '2': 'sausage', '3':'spam'}
a = mydict.items()
b = mydict.keys()
c = mydict.values()
print(a,'\n',b,c)

if '1' in b:
    print(True)

mydict['4'] = 'cow'
print(id(a), id(mydict))
print(a, mydict)

import pickle
f = open("mypickle", "wb")
pickle.dump(mydict, f)
f.close()

print("save!!")

if __name__ == '__main__':
    pass