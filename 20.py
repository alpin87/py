import random

com = random.randrange(1,21)
user = -1
while com != user :
    user = int(input("입력 : "))
    if com == user :
        print("맞췄습니다.")
        break
    elif user < com :
        print("더 큰수 입니다.")
    else :
        print("더 작은 수 입니다")
    
