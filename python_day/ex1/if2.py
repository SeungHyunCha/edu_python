import random
r = random.randint(1,3)
glist = ['a','b','c']
print(r,glist[r-1])

gbb = input("1,2,3>>")
gbb = int(gbb)

if r == gbb:
    result = "draw"
elif r == 1:
    if gbb == 2:
        result = "win"
    else:
        result = "lose"
elif r == 2:
    if gbb == 1:
        result = 'lose'
    else:
        result = 'win'

else:
    if gbb == 1:
        result = 'win'
    else:
        result = 'lose'
        
print("r = %s, gbb = %s, %s" %(r, gbb, result))