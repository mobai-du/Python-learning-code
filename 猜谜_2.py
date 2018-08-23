from random import randint
num = randint(1,100)

print("请输入你的数字")

bingo = False

while bingo == False:
    user_num = int(input())

    if user_num < num:
        print("small")
    elif user_num > num:
        print("big")
    else:
        print("bingo")
        bingo = True
