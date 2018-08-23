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
# print(menu.items())

while True:
    for k in menu:
        print(k)
    province = input("请输入省份，按q退出,按b返回上一层！\n")
    if province in menu:
        while True:
            for k in menu[province]:
                print(k)
            city = input("请输入城市，按q退出,按Q返回上一层！\n")
            if city in menu[province]:
                while True:
                    for k in menu[province][city]:
                        print(k)
                    area = input("请输入区，按q退出,按Q返回上一层！\n")
                    if k in menu[province][city]:
                        for k in menu[province][city][area]:
                            print(k)
                            print("已到最后一层！")
                        pass
                    elif area == 'b':
                        break
                    elif area == 'q':
                        exit()
                    else:
                        print("输入错误")
            elif city == 'b':
                break
            elif city == 'q':
                exit()
            else:
                print("输入错误")
    else:
        print("输入错误")