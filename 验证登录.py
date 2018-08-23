import codecs
import os


user_list = ['du','peng','ju']
pw_list = [123,456,789]

f = open("123.txt","r",encoding="utf-8")#'r'表示只读，如果123.txt不存在，会自动创建一个文件，字符编码是utf-8
lock_file = f.read()#读取整个文件
f.close()#关闭文件
n = 0
while n < 3:
    print("请输入用户名密码")
    username = input()
    pw = int(input())
    if username in lock_file:#判断用户名是否已被锁住
        print("此账户已被锁定")
        exit()
    elif username in user_list and pw in pw_list:
        print("登录成功,")
        break
    else:
        print("登录失败")
        n += 1



    if n == 3:
        print("此账户将被锁定")
        f = open("123.txt","a")#'a'表示append，表示不清除原有数据，在原有数据之后，继续写数据
        f.write("%s\n"%username)#写入文件
        f.close()



