# import sys
# print(sys.getrecursionlimit())
#
# def calc(n):
#     n = int(n/2)
#     print(n)
#     calc(n)
#
# calc(10)


# def calc(n):
#     n = int(n/2)
#     print(n)
#     if n > 0:
#         calc(n)
#     print(n)
# calc(10)


def calc(n,count):
    print(n,count)
    if count < 5:
        return calc(n/2,count+1)
    else:
        return n
res = calc(100,1)
print('res',res)