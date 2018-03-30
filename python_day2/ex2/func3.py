g_var = 77

def fn1():
    global g_var
    g_var += 100
    print(g_var)
    
fn1()
print(g_var)

a = dir(__builtins__)

b = globals()
c = list(b.keys())
print(b)
print(c)

for i in c:
    print(i)
    print(b[i])