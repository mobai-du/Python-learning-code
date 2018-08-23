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
current_layer = menu  # 实现动态循环
parent_layer = []  # 保存所有父级，最后一个元素永远是父亲级

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0: continue
    if choice in current_layer:
        # parent_layer=current_layer
        parent_layer.append(current_layer)  # 把当前级加入父亲级称为列表最后一个元素
        # 下一次循环，当输入return，就可以直接取列表最后一个值
        current_layer = current_layer[choice]
    elif choice == "return":
        # current_layer=parent_layer
        current_layer = parent_layer.pop()  # 取出列表最后一个值，因为他就是当前层的父亲级
    elif choice == "quit":
        break
    else:
        print("no item")