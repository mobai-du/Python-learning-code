def add(x,y,f):
    return f(x) + f(y)
res = add(3,-10,abs)
print(res)