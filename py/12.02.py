# 실습
# print('나는 빵을 %d개 먹었다.' %2)
# print('나는 빵을 %d%s 우유 %d개 먹었다.' %(2,'와',1))
# print(f'나는 빵을 {2}{'와'} 우유 {1}개 먹었다.')
# print('1인치는 %.2fcm입니다.' %2.54)

# friends = "고찬국 김다운 김민창"
# list = friends.split(" ")
# print(list)

# email = "lkj10009@gmail.com"
# print(email.split('@'))
# greeting = "   Hi, Jerry   "
# greeting2 = "Hi, Jerry   "

# print(greeting)
# print(greeting.strip())
# print(greeting.lstrip())

# print(greeting2.rstrip())

# # 실습 2
# # 몫과 나머지를 이용하여 추출하는 방법
# num1 = int(input()) #1
# num2 = int(input())#2
# num3 = num2 % 10
# num4 = (num2 // 10) % 10
# num5 = num2 //100
# a = print(num1*(num3)) #3
# b = print(num1*(num4)) #4
# c = print(num1*(num5)) #5
# d = print(num1*num2) #6

# # 리스트를 이용하는 방법
# a = input() # 472
# b = input() # 385

# print(int(a) * int(b[2])) # 472*5
# print(int(a) * int(b[1])) # 472*8
# print(int(a) * int(b[0])) # 472*3
# print(int(a) * int(b)) # 472*385
# in 연산자
# cart = ["계란", "마늘", "라면", "커피"]

# print('라면' in cart)
# print('콩나물' in cart)

# if True:
#     print("감사합니다.")
# a = int(input())
# if (a%2)==0:
#     print("짝수")
# elif (a%2)==1:
#     print("홀수")    



# for i in range(100):  # 예를 들어 100번 실행
#     a = int(input("숫자를 입력하세요: "))
#     if (a % 2) == 0:  # 짝수일 경우
#         print("짝수입니다.")
#         break  # 종료
#     else:  # 홀수일 경우
#         print("홀수입니다. 다시 입력하세요.")
#         continue  # 다시 루프

# for i in range(100):  # 최대 100번 반복
#     grade = int(input("점수를 입력해주세요: "))
#     if 0 <= grade <= 100:  # 유효한 점수인지 확인
#         if grade < 60:
#             print("E")
#         elif grade < 70:
#             print("D")
#         elif grade < 80:
#             print("C")
#         elif grade < 90:
#             print("B")
#         else:
#             print("A")
#         break 
#     else:
#         continue 



age = int(input("나이를 숫자로 입력해 주세요: "))
method = input("결제 방법을 입력해주세요.('카드' or '현금'): ")
if(method!="카드" or method!="현금"):
    method = input("결제 방법이 다릅니다. 다시 입력해주세요.('카드' or '현금'): ")

if age < 8:
    payment = "무료"
elif age < 14:
    payment = "450원"
elif age < 20:
    if method == "카드":
        payment = "720원"
    else:
        payment = "1000원"
elif age < 75:
    if method == "카드":
        payment = "1200원"
    else:
        payment = "1300원"
else:
    payment = "무료"

print(f"{age}세의 {method} 요금은 {payment} 입니다.")
