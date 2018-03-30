import pickle
f = open("mypickle", "rb")
mydict2 = pickle.load(f)
print(mydict2)
f.close()

if __name__ == '__main__':
    pass