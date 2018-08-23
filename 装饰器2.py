
user_status = False#用户登录了就把这个改成True


def login(auth):#把要执行的模块从这里传进来   henan
    def outer(func):
        def inner(*arg,**kwargs):#再定义一层函数
            _username = 'alex'#假装这是DB里存的信息
            _password = 'abc123'#假装这是DB里存的信息
            global user_status

            if user_status == False:
                username = input('user:')
                password = input('password:')

                if username == _username and password == _password:
                    print("welcome login...")
                    user_status = True
                else:
                    print("wrong username or password!")
            else:
                print("用户已登录，验证通过")
            if user_status:
                func(*arg,**kwargs)#henan()
        return  inner
    return outer


def home():
    print("---首页---")
def america():
    print("----欧美专区----")
@login('wx')
def japan():
    print("----日韩专区----")
@login('qqq')    #login('qq')先执行一遍，返回outer的函数，在调用henan(),在执行，在返回inner()函数，在运行，得到结果
def henan(style):
    print("----河南专区----",style)

# henan = login(henan)#inner
# print(henan)
japan()
henan('3p')#inner()

