
age = 22
n=0
while n < 3:
    print("input you age")
    user_age = int(input())
    if user_age < age:
        print("small")
    elif user_age > age:
        print("big")
    else:
        print("bingo")
        break
    n += 1

    if n==3:
        choice = input("请问你还想继续游戏吗？y|n")
        if choice=='y':
            n=0
        else:
            break




