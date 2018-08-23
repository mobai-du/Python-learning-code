import os

goods = [['电脑', 1999], ['鼠标', 10], ['游艇', 20], ['美女', 998]]
username = "du"
password = '123'

shopping_cart = []
user = input("please you input username!\n")
passwd = input("please you input password!\n")
if os.path.exists("111.txt"):  # 判断111.txt,是否存在
    f = open("111.txt", "r", encoding="utf-8")  # 'r'表示只读，字符编码是utf-8
else:
    f = open("111.txt", "w+")  # 创建一个111txt,'w'表示写
file = f.read()  # 读取整个文件

if user == username and passwd == password:
    print(".......welcome .....")
    wages = input("please you input wages\n")
    if wages.isdigit():
        wages = int(wages)
        print("you input wages is %s " % (wages))
    else:
        print("输入有误")
        exit()
    print("上次购买的商品为 %s  " % (file))
    while True:
        str = '商品列表'
        str1= '已购买商品'
        print(str.center(20,"-"))
        for index, i in enumerate(goods):
            print("   %s      %s     %s    " % (index, i[0], i[1]))

        choice = input("please your input number:")
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(goods):
                m = goods[choice]#将大列表装换成小列表，获取索引，得到价格
                print("  %s    商品已加入购物车\033[92m" % (m[0]))
                if wages > m[1]:
                    wages -= m[1]
                    shopping_cart.append(m)
                    print("你已经购买   %s  商品,你的余额为  %s\033[94m" % (m[0], wages))
                else:
                    print("无法购买该商品，你的余额不足\033[95m")
            else:
                print("商品不存在")
        elif choice == 'q':
            if len(shopping_cart) > 0:
                print(str1.center(20,'-'))
                for index, i in enumerate(shopping_cart):
                    print("   %s      %s     %s    " % (index, i[0], i[1]))
                f = open('111.txt', 'a+',encoding="utf-8")
                f.writelines("%s %s" % (shopping_cart,wages))
                f.close()
                break

else:
    print("input error,please again\n")
