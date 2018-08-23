#匿名函数


# def calc(x,y):
#     return x*y
#
#
# func = lambda x,y:x*y  #声明一个匿名函数
# print(func(3,8))

data = list(range(10))
print(data)

# for index, i in enumerate(data):
#     data[index] = i*i
#
# print(data)

def f2(n):
    return n*n
l = list(map(lambda x:x*x, data))
print(l)