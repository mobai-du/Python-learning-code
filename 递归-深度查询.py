'''
条件
1.打印所有节点，
2.输入一个节点，沙河，你要遍历找，找到了，就打印它，并返回True

'''
menus = [
    {
        'text':'北京',
        'children':[
            {'text':'朝阳','children':[]},
            {'text':'昌平','children':[
                {'text':'沙河','children':[]},
                {'text':'回龙观','children':[]},
            ]},
        ]
    },
    {
        'text':'上海',
        'children':[
            {'text':'宝山','children':[]},
            {'text':'金山','children':[]},
        ]
    }
]
# def recu_Menu(menu):
#     for sub_menu in menu:
#         menu_text = sub_menu['text']
#         menu_children = sub_menu['children']
#         print(menu_text)
#         recu_Menu(menu_children)
# recu_Menu(menus)


flag = False
def recu_Menu_node(menu,node,layer):
    global flag
    for sub_menu in menu:
        menu_text = sub_menu['text']
        menu_children = sub_menu['children']
        if node == menu_text:
            print('找到%s在第%s层'%(node,layer))
            flag = True
            return flag
        else:
            recu_Menu_node(menu_children,node,layer +1)
            print("menu_text=",menu_text)
    return flag
node_str = input(">>>")
print(recu_Menu_node(menus,node_str,1))