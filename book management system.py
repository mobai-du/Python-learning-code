import  os
books=[['Python基础编程',100],['Python进阶编程',100],['Python高级编程',100],['Django入门指南',100]]
# users = {'name':'alex','pw':'alex123',#管理员
#          'name':'pizza','pw':'pizza123',#教师
#          'name':'john','pw':'john123',}#学生
users = [['alex','alex123'],#管理员
         ['pizza','pizza123'],#教师
         ['john','john123']]#学生

if os.path.exists('lock.txt'):
    f = open("lock.txt",'r',encoding="utf-8")
else:
    f = open("lock.txt","w+")
lock_file = f.read()
f.close()
flag = '图书管理系统'
flag1= '选项'
books_list = '书籍列表'
name_1 = '添加用户'
name_2 = '删除用户'
name_3 = '添加书籍'
name_4 = '删除书籍'
print(flag.center(50, '-'))
shopping_cart = []
wages = 3000
n = 0
if os.path.exists("books_buy.txt"):
    f = open("books_buy.txt", "r", encoding="utf-8")
else:
    f = open("books_buy.txt", "w+")
file = f.read()
choice = input("请选择你的身份：[1]管理员，[2]教师，[3]学生，按q退出")
if choice == '1':
    print("请输入管理员账号及密码")
    while n < 3:
        username = input("输入用户名")
        password = input("输入密码")
        if username in lock_file:
            print("此账户已锁定")
            break
        elif [username,password] == users[0]:
            print("欢迎你登录图书管理系统，你的身份是管理员")
            print('''
              功能选项
             0 添加用户
             1 删除用户
             2 添加书籍
             3 删除书籍
            ''')
            while True:
                choice = input("请选择功能，按q退出")
                if choice == '0':
                    print(name_1.center(50,'*'))
                    users_add = input("输入用户名")
                    pw_add = input("输入密码")
                    users.append([users_add,pw_add])
                    print('添加成功',users)
                elif choice == '1':
                    print(name_2.center(50,'*'))
                    users_del = input("输入用户名，进行删除")
                    users.remove(users_del)
                    print('删除成功',users)
                elif choice == '2':
                    print(name_3.center(50,'*'))
                    books_add= input("输入书籍名称")
                    books.append(books_add)
                    print("添加成功",books)
                elif choice == '3':
                    print(name_4.center(50,"*"))
                    book_del = input("输入书籍名称，进行删除")
                    books.remove(book_del)
                    print("删除成功",books)
                elif choice == 'q':
                    exit()
                else:
                    print("输入有误")




        else:
            print('登录失败')
            n += 1

        if n ==3:
            print("此账户将被锁定")
            with open('lock.txt','w') as f:
                f.write("%s"%username)


elif choice == '2':
    print("请输入教师账号及密码")
    while n < 3:
        username = input("输入用户名")
        password = input("输入密码")
        if username in lock_file:
            print("此账户已锁定")
            break
        elif [username,password] == users[1]:
            print("欢迎你登录图书管理系统，你的身份是教师")
            # while True:
            print('''
                选择功能
                1.借书
                2.归还
            ''')
            # while True:
            choice1 = input()
            if choice1 == '1':
                print(books_list.center(50, '-'))
                for index, i in enumerate(books):
                    print(" %s   %s   %s  " % (index, i[0], i[1]))
            while True:
                if choice1 == '1':
                    choice1_1 = input("请选择你要借阅的书")
                    if choice1_1.isdigit():
                        choice1_1 = int(choice1_1)
                        if choice1_1 >= 0 and choice1_1 < len(books):
                            m = books[choice1_1]
                            print("  %s  已加入购物车"%m[0])
                            if wages > m[1]:
                                wages -= m[1]
                                shopping_cart.append(m)
                                print("你已借阅  %s  ，余额为  %s "%(m[0],wages))
                            else:
                                print("余额不足")
                        else:
                            print("书不存在")
                    elif choice1_1 == 'q':

                        if len(shopping_cart) > 0:
                            books.remove(m)
                            print(books_list.center(50,'-'))
                            print("剩余书籍:",books)
                            for index,i  in enumerate(shopping_cart):
                                print("%s %s %s "%(index,i[0],i[1]))
                                f = open('books_buy.txt', 'a+', encoding="utf-8")
                                f.writelines("%s %s" % (shopping_cart, wages))
                                f.close()
                            exit()


                elif choice1 == '2':
                    print('''
                    书籍列表
                    0 <Python基础编程>,-100
                    1 <Python进阶编程>,-100 
                    2 <Python高级编程>,-100 
                    3 <Django入门指南>，-100
                    ''')
                    choice1_2 = input("请选择你要归还的书,按q退出")
                    if choice1_2 == '0':
                        books.append(['Python基础编程',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == '1':
                        books.append(['Python进阶编程',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == '2':
                        books.append(['Python高级编程',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == '3':
                        books.append(['Django入门指南',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == 'q':
                        exit()
                    else:
                        print("输入有误")



        else:
            print('登录失败')
            n += 1

        if n ==3:
            print("此账户将被锁定")
            with open('lock.txt','w') as f:
                f.write("%s"%username)



elif choice == '3':
    print("请输入学生账号及密码")
    while n < 3:
        username = input("输入用户名")
        password = input("输入密码")
        if username in lock_file:
            print("此账户已锁定")
            break
        elif [username,password] == users[2]:
            print("欢迎你登录图书管理系统，你的身份是学生,按q退出")
            print('''
                选择功能
                1.借书
                2.归还
            ''')
            choice1 = input()
            if choice1 == '1':
                print(books_list.center(50, '-'))
                for index, i in enumerate(books):
                    print(" %s   %s   %s  " % (index, i[0], i[1]))
            while True:
                if choice1 == '1':
                    choice1_1 = input("请选择你要借阅的书")
                    if choice1_1.isdigit():
                        choice1_1 = int(choice1_1)
                        if choice1_1 >= 0 and choice1_1 < len(books):
                            m = books[choice1_1]
                            print("  %s  已加入购物车"%m[0])
                            if wages > m[1]:
                                wages -= m[1]
                                shopping_cart.append(m)
                                print("你已借阅  %s  ，余额为  %s "%(m[0],wages))
                            else:
                                print("余额不足")
                        else:
                            print("书不存在")
                    elif choice1_1 == 'q':
                        if len(shopping_cart) > 0:
                            books.remove(m)
                            print(books_list.center(50,'-'))
                            print("剩余书籍:",books)
                            for index,i  in enumerate(shopping_cart):
                                print("%s %s %s "%(index,i[0],i[1]))
                                f = open('books_buy.txt', 'a+', encoding="utf-8")
                                f.writelines("%s %s" % (shopping_cart, wages))
                                f.close()
                            exit()


                elif choice1 == '2':
                    print('''
                    书籍列表
                    0 <Python基础编程>,-100
                    1 <Python进阶编程>,-100 
                    2 <Python高级编程>,-100 
                    3 <Django入门指南>，-100
                    ''')
                    choice1_2 = input("请选择你要归还的书，按q退出")
                    if choice1_2 == '0':
                        books.append(['Python基础编程',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == '1':
                        books.append(['Python进阶编程',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == '2':
                        books.append(['Python高级编程',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == '3':
                        books.append(['Django入门指南',100])
                        wages = wages + 100
                        print("归还成功,薪资增加100",books,wages)
                    elif choice1_2 == 'q':
                        exit()
                    else:
                        print("输入有误")



        else:
            print('登录失败')
            n += 1

        if n ==3:
            print("此账户将被锁定")
            with open('lock.txt','w') as f:
                f.write("%s"%username)

elif choice == 'q':
    exit()
else:
    print("输入有误，请检查")


