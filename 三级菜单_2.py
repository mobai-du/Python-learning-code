menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {}
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            '人民银行': {
                '炸鸡店': {}
            },
        },
        '闸北': {
            '火车站': {
                '携程': {}
            },
        },
        '浦东': {},
    },
    '山东': {},
}

exit_flag = False#标志位,只要不为True,循环会一直执行
while not exit_flag:
    for i in menu:#循环打印data
        print(i)
    choice = input("请输入>>>")
    if choice in menu:#判断choice是否在data中
        while not exit_flag:
            for i2 in menu[choice]:
                print(i2)
            choice2 = input("请输入>>>")
            if choice2 in menu[choice]:
                while not exit_flag:
                    for i3 in menu[choice][choice2]:
                        print(i3)
                    choice3 = input("请输入>>>")
                    if choice3 in menu[choice][choice2]:
                        for i4 in menu[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("最后一层,请输入b返回或输入q结束>>>")
                        if choice4 == 'b':
                            pass#直接跳过,如果不加pass的话会报错
                        elif choice4 == 'q':
                            exit_flag = True
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            elif choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True
    elif choice == 'q':
        exit_flag = True