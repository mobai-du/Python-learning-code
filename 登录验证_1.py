import os

user_list = ['du', 'peng', 'ju']
pw_list = [123, 456, 789]

if os.path.exists("123.txt"):  # 判断123.txt,是否存在
    f = open("123.txt", "r+", encoding="utf-8")  # 'r'表示只读，如果123.txt不存在，会自动创建一个文件，字符编码是utf-8
else:
    f = open("123.txt", "w+")
lock_file = f.read()  # 读取整个文件

n = 0
while n < 3:
#    print("")
    username = input("请输入用户名:").strip()
    pw = input("密码请输入数字：").strip()
    if pw.isdigit():
        int(pw)
    else:
        n += 1
        continue
    if username in lock_file:  # 判断用户名是否已被锁住
        print("此账户已被锁定")
        break
    elif username in user_list and pw in pw_list:
        print("登录成功,")
        break
    else:
        print("登录失败")
        n += 1
        if n == 3:
            print("此账户将被锁定")
            f.write("%s\n" % username)  # 写入文件
f.close()