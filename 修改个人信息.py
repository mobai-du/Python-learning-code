user_data = {'alex':'abc123','rain':'rain','shanshan':'shanshan'}
data= ['李杰','22','Teacher','IT','123']
       # {'name':'rainwang','age':'27,','job':'engineer','Dept':'IT','phone':'456'},
data_1 = {'name':'杜姗姗','age':'22','job':'model','Dept':'PR','phone':'789'}
flag = 'welcome alex'
def login():
    while True:
        user = input("username:")
        if user not in user_data:
            print("此用户不存在")
            continue
        else:
            break

    passwd = input("password:")
    pwd = user_data.get(user)
    while True:
        if passwd == pwd:
            print(flag.center(30, '-'))
            print('''
1.打印个人信息
2.修改个人信息
3.修改密码
        ''')
            # for i in data_1.values():
            #     print(i)

            # L = i
            choose_1 = input('>>>')
            if choose_1 == '1':
                #     info = """
                # ----------------------
                # Name:  %s
                # Age:   %s
                # Job:   %s
                # Dept:  %s
                # Phone: %s
                # ----------------------
                # """ % (data_1.get("name"),data_1.get("age"),data_1.get("job"),data_1.get("Dept"),data_1.get("phone"),)
                #     print(info)
                info = """
            ----------------------
            Name:  %s
            Age:   %s
            Job:   %s
            Dept:  %s
            Phone: %s
            ----------------------
            """ % (data[0], data[1], data[2], data[3], data[4])
                print(info)

            if choose_1 == '2':
                print('person data:', data)
                for index, k in enumerate(data):
                    print(index, k)
                choose_2 = input(">>>")
                if choose_2 == '0':
                    print("old_str:", data[0])
                    new_str = input("输入新的")
                    if new_str == "":
                        print("不能为空")
                        print(data)
                    else:
                        data[0] = new_str
                        print(data)
                if choose_2 == '1':
                    print("old_str:", data[1])
                    new_str = input("输入新的")
                    if new_str == "":
                        print("不能为空")
                        print(data)
                    else:
                        data[1] = new_str
                        print(data)
                if choose_2 == '2':
                    print("old_str:", data[2])
                    new_str = input("输入新的")
                    if new_str == "":
                        print("不能为空")
                        print(data)
                    else:
                        data[2] = new_str
                        print(data)
                if choose_2 == '3':
                    print("old_str:", data[3])
                    new_str = input("输入新的")
                    if new_str == "":
                        print("不能为空")
                        print(data)
                    else:
                        data[3] = new_str
                        print(data)
                if choose_2 == '4':
                    print("old_str:", data[4])
                    new_str = input("输入新的")
                    if new_str == "":
                        print("不能为空")
                        print(data)
                    else:
                        data[4] = new_str
                        print(data)
            if choose_1 == '3':
                for values in user_data.values():
                    print(values)


    else:
        print('密码错误！')

login()