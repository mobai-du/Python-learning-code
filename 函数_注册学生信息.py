def   stu_register(name, age, course = 'PY', country = 'CN'):
    print("----注册学生信息-----")
    print("姓名",name)
    print("age",age)
    print("国籍",country)
    print("课程",course)
    if age > 22:
        return False
    else:
        return True


registration_status = stu_register("张三",22,"china",'python')

if registration_status:
    print("注册成功")

else:
    print("注册失败")