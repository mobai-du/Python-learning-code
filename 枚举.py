names = ['a','b','c','d','e']

# count = 0
# for i in names:
#     print(count,i)
#     count += 1
# for i in enumerate(names):#枚举
#     print(i)

for index,i in enumerate(names):
#    print(index, i)
    if index%2 == 0:
        names[index] = -1
        print(index, i)
print(names)



