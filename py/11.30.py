# 변수의 이해 및 f 문자열 포메팅

# messi= "FCB"
# print(messi)
# messi = "축구"
# print(messi)
# print(f"나는 {messi}를 좋아합니다.")
# # 숫자형
# print(type(77))

# # 실수형
# print(type(7.2))

# # 문자형
# print(type("배드민턴"))
# print("배드\'민턴")
# print("what\'s")

# print("배드\t민턴")
# print("배드\n민턴")

# # 진수 표현하기
# num = 10
# b_num = 0b1010
# h_num = 0xA

# print(num)
# print(b_num)
# print(h_num)

# # 진수 표현 함수
# print(bin(10))
# print(bin(65))
# print(hex(10))
# print(hex(65))

# # 아스키 코드값과 문자
# print(ord('0'))
# print(ord('A'))
# print(chr(48))
# print(chr(65))

# print(3//2)
# print(3.25//2)
# print(3%2)
# print(3.25%2)
# print(2**3)
# print(2**10)

# bread = 30
# count = 4

# print("빵의 개수 : ", bread//count)
# print("남은 빵의 개수 : ", bread%count)

# # 복합 대입 연산자
# a=3
# a+=1
# print(a)

# print("럭키"+"비키")

# player = input("너의 최애 선수는?") # 입력
# print(player) # 출력

# a = input("1+1=")
# b=int(a)
# a = int(input("1+1="))
# print(a+2)
# a = input("1+1=")
# print(int(a)+2)

# print("|\\_/|")
# print("|\\q p|\t/}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`\t|")
# print("||_/=\\\\__|")

# #1
# name = input("이름을 입력하세요 : ")
# age = input("나이를 입력하세요 : ")
# print("안녕하세요! " + name +"님"+"("+ age+"세)")

# #2
# name = input("이름을 입력하세요 : ")
# birth = int(input("태어난 년도를 입력하세요 : "))
# year = int(input("올해 년도를 입력하세요 : "))
# age = year - birth
# print("올해는 "+str(year)+"년,"+str(name)+"님의 나이는 "+str(age+ 1)+"세입니다.")

# a =[]
# b = [1,2,3,4]
# c = ["메시", "호날두"]
# print(len(c))
# c[1] = '네이마르'
# print(c)
# del c[1]
# print(c)

# # 리스트 슬라이싱
# seasons = ["봄", "여름", "가을", "겨울"]
# print(seasons[:-1])
# print(seasons[0:1])  # ['봄']
# print(seasons[0:2])  # ['봄', '여름']
# print(seasons[:2])   # ['봄', '여름']
# print(seasons[1:])   # ['여름', '가을', '겨울']
# print(seasons[2:])   # ['가을', '겨울']
# print(seasons[1:3])  # ['여름', '가을']

# a=[1,2,5,3,4,5,6,7,8]
# a.sort()
# print(a)

# a = [3,4,2,1]
# a.sort()
# print(a)

# b = ["a", "c", "b", "d"] 
# b.sort() # 알파벳 순 정렬
# print(b)

# c = ["1", "13", "11", "2"]
# c.sort() # 사전순으로 정렬
# print(c)

# d = ["카리나","윈터"]
# d.append("장원영")
# print(d)
# d.remove("윈터")
# print(d)
# d.insert(1,"안유진")
# print(d)

# d = ["강남", "강북", "서", "asdfd", "서", "서"]

# first = d.index("서")+1
# print(first + d[first:].index("서"))

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
# 1. 2번 인덱스 값 출력
print(rainbow[2])

# 2. 알파벳 순서로 정렬한 값 출력
rainbow.sort()
print(rainbow)

# 3. 좋아하는 색 맨 마지막에 추가하기
rainbow.append("skyblue")
print(rainbow)

# 4. 3 ~ 6번째 값 삭제하기
del rainbow[3:7]
print(rainbow)