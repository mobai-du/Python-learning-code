# staff_id = 0
# data = {{'name':'alex','age':'22','phone':'136','dept':'IT','enroll_date':'2013-04-01'},
#         {'name':'jack','age':'30','phone':'137','dept':'HR','enroll_date':'2014-04-01'},
#         {'name':'rain','age':'25','phone':'138','dept':'Sales','enroll_date':'2015-04-01'},
#         {'name':'mack','age':'40','phone':'139','dept':'HR','enroll_date':'2016-04-01'},
#         }
# print(data)
# print(type(data))
# data = ['alex','22','136','IT','2013-04-01']
# f = open('information.txt','a+',)
# # f.write("1,alex,22,136,IT,2013-04-01")
# # f.write("\n2,jack,30,137,HR,2014-04-01")
# # f.write("\n3,rain,25,138,Sales,2015-04-01")
# f.write("\n4,mack,40,139,HR,2016-04-01")
# f.close()
with open("information.txt",'r+') as f:
    date = f.readlines()
    print(date)

    info = '''
    0 查询信息
    1 增加信息
    2 删除信息
    3 修改信息
    4 退出
    '''
# print(type(date))
# def find_date():
    # while True:
    #     userdate = input("查询>>>")
    #     if len(userdate) == 0:continue
    #     for line in date:
    #         find_date_1 = line.split(',',5)
    #         if  userdate in find_date_1:
    #             print(find_date_1)
    #     if userdate == 'q':
    #         print(info)
    #         break
# find_date()

# def add_date(*arg,**kwargs):
#     while True:
#         user_date = input("增加>>>")
#         if len(user_date) == 0:continue
#         date.append(user_date.strip())
#         print(date)
#         if user_date == 'q':
#             print(info)
#             break
# add_date()

# def del_date():
#     while True:
#         user_date_1 = input("删除>>>")
#         if len(user_date_1) == 0:continue
#         for a in date:
#             del_date_1 = a.split(',',5)
#             if user_date_1 in del_date_1:
#                date.remove(a)
#                print(date)
#         if user_date_1 == 'q':
#             print(info)
#             break
# del_date()

def mod_date():
    while True:
        info1 = '''
                  1 修改名字
                  2 修改年龄
                  3 修改手机号码
                  4 修改职业
                  5 修改时间
                  '''
        print(info1)
        # user_date_2 = input("修改>>>")
        # if len(user_date_2) == 0:continue
        for b in date:
            c = b.split(',',5)
            print(type(c[1]))
            print(c)


        choose = input(">>>")
        if choose == '1':
            old_user = input("输入旧名字>>>")
            new_user = input("输入新名字>>>")
            if old_user in c[1]:
                print("good")
                c.append(c[1].replace(old_user,new_user))
                # print(d)

            # print(c)
            # if user_date_2 == c[0] or user_date_2 == c[1]:
            #     c.append(b.replace(c[0],user_date_2))
            # # print(c[1])
            #     print(c)
        # if user_date_2 == 'q':
        #     print(info)
        #     break

mod_date()

# def managament():
#
#     print(info)
#     while True:
#         choose = input("输入选项>>>")
#         if choose == '0':
#             find_date()
#         elif choose == '1':
#             add_date()
#         elif choose == '2':
#             del_date()
#         elif choose == '3':
#             mod_date()
#         elif choose == '4':
#             exit()
#
# managament()