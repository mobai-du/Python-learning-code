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
parent_layer = []
while True:
        for key in menu:
            print(key)
        choose = input("请选择，输入b返回上一级菜单，输入q退出菜单:").strip()
        if choose in menu:
            parent_layer.append(menu)
            menu = menu[choose]
        elif choose == 'b':
            if parent_layer:
                menu = parent_layer.pop()
        elif choose == 'q':
            exit()
        else:
            print("\n输入有误，请重新输入\n")