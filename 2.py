# 1번 2번
# choice= bool(input('만날까? 말까? (1/0) 입력 :'))
# print("오늘부터 1일 ")if choice else print("다음기회에")


# 3번
# import random
# a = random.randrange(0, 3)
# if a == 0:
#     print('제주도 출발')
# elif a == 1:
#     print("사이판")
# else:
#     print("하와이")

# # 4번
# import random
# com= random.randrange(3)
# user= int(input('가위0 바위1 보2 선택: '))
# print('user= %d, com= %d' % (user, com))

# if user == com :
#     print("비겼습니다")
# elif (user == 0 and com == 2) or(user == 1 and com == 0) or (user == 2 and com == 1) :
#     print('user win')
# else :
#     print('com win')

## 5번
# import random
# com= random.randrange(3)
# cnt = 1

# while (1) : 
#     user = int(input('가위0 바위1 보2 선택: '))
#     if user <= 2 :
#         break
#     cnt += 1
# if user == com :
#     print("비겼습니다")
# elif (user == 0 and com == 2) or(user == 1 and com == 0) or (user == 2 and com == 1) :
#     print('user win')
# else :
#     print('com win')
#     print("유저 : %d 컴 : %d 횟수 : %d" % (user, com, cnt))


# a = int(input('마지막값 입력 :'))
# i = 2
# sum = 0
# while (i <= a):
#     sum = sum + i
#     i = i + 2
#     print("%d" % sum)
    

# select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

# if select == 1 :
#     nexp = input(' ** 수식 입력 : ')
#     ans = eval(nexp)
#     print(" %s 결과는 %5.1f입니다" % (nexp, ans))
# elif select == 2 :
#     n1 = int(input(' ** 첫번째 숫자 입력 : '))
#     n2 = int(input(' ** 두번째 숫자 입력 : '))
#     ans = 0
#     for i in range(n1, n2+1) :
#         ans = ans + i
#     print('%d+...+%d는 %d입니다' % (n1,n2,ans))
# else :
#     print('1, 2만 입력하세요')

for dan in range(2, 10):
    print('\n%d단 : ' % dan, end = '')
    for n in range(1,10):
        print('%d x %d = %d' % (dan, n, dan * n), end = '')