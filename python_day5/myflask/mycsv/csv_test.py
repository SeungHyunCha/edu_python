import csv

nms = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
# f = open('number2.csv','w')
f = open('number2.csv','w',newline = "")
with f: # automatic insert f.close()
    writer = csv.writer(f)
    for row in nms:
        writer.writerow(row)
        
print('end')

f = open('number2.csv','r')
with f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
    
