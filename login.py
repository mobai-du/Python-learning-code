username = 'dupeng'
passwd = 123456

n = 0
while n < 3:
    print("请输入用户名密码")
    user_name = input()
    user_pw = int(input())
    if username == user_name and passwd == user_pw:
        print("登录成功，欢迎你")
        break
    else:
        print("用户名密码有误,请重新输入")
        n += 1
    if n == 3:
        break