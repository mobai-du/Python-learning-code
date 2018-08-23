products = [['iphone',6888],['macpro',14800],['xiaomi6',2499],['coffee',31],['book',80],['nike shoes',799]]
print("---------商品列表--------------")
for index,p in enumerate(products):
    # print(index,p[0],p[1])
    print("%s    %s    %s   "%(index,p[0],p[1]))