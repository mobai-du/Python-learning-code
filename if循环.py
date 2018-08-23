print("input your score")
user_score = int(input())

if  80 <= user_score < 100:
    print("优秀")
elif 60 <= user_score <80:
    print("良好")
elif user_score>100:
    print("输入错误")
else:
    print("不及格")