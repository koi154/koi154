# 모듈 불러오기 방법1. import 모듈이름
# import calc_module # 컨트롤 누르고 클릭

# print(calc_module.add(2,3))
# print(calc_module.sub(2,3))
# print(calc_module.mul(2,3))
# print(calc_module.div(2,3))

# 모듈 불러오기 방법2. from 모듈이름 import 함수이름
# from calc_module import add
# from calc_module import * # 모듈의 모든 함수를 가져올 떄

# print(add(1,2))
# calc_moudule.add() #안됨

# 모듈 불러오기 방법3. import 모듈이름 as 이름
# import calc_module as cm
# print(cm,add(1,2))

# import math

# print(math.floor(3.141592))
# print(math.ceil(3.141592))
# print(math.sqrt(9))

# from math import floor, ceil
# print(floor(3.141592))
# print(ceil(3.141592))

# import random

# print(random.randint(1,5)) #1,5포함 임의의 정수 리턴
# print(random.uniform(1,5)) #1,5포함 임의의실수 리턴
# print(random.random()) # 0<=x<1 임의의실수 리턴
# print(random.randrange(1,5)) # 1부터 5사의 임의의 정수 리턴 (5 미포함)
# print(random.randrange(1,5,2)) # 2만큼 지정된 간격으로 임의의 정수리턴

#실습3 up and down 게임
# import random

# com = random.randint(1,100)
# min_v = 1 #최소
# max_v = 100 #최대
# score = 100 #100점 시작
# count = 0 #횟수 0시작

# while True:
#     try:
#         guess = int(input("숫자 입력(%d ~ %d): " % (min_v, max_v))) 
#         count += 1
#         if guess < 0 or guess > 100:
#             print("입력 범위를 초과했어요.")
#         elif com == guess:
#             print (f"정답이에요 랜덤 숫자는 {com}입니다.!!")
#             print(f"총 {count}회 만에 맞췄습니다.")
#             print(f"최종점수 {score}입니다.")
#             break
#         elif com > guess:
#             print (f"랜덤수보다 작아요")
#             min_v = guess 
#             score -= 10
#         else:
#             print("랜덤수보다 커요")
#             max_v = guess 
#             score -= 10
#     except ValueError:
#         print("숫자만 입력 가능합니다.")

#실습. 로또 번호뽑기
# import random

# lotto = []
# num = random.randint(1,45)

# for i in range(6):
#     while num in lotto:
#         num = random.randint(1,45)
#     lotto.append(num)
# lotto.sort()
# print(f"로또번호 : {lotto}")


#로또 번호뽑기 
# lotto = random.sample(range(1,46), 6)
# print(sorted(lotto))

# import datetime

# now = datetime.datetime.today()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# print(f'{now.year}년 {now.month}월 {now.day}일')
# print(f'{now.hour}시 {now.minute}분 {now.second}초')

# 나이가 100세 되는 해의 연도 계산
# import datetime

# today = datetime.date.today()
# print(today.year)

# age = int(input("나이 입력: "))

# result = today.year + (100 - age)
# print("100세 되는 해는" + str(result) + "년 입니다.")

# 지나온 날짜 계산하기
# import datetime

# print( " 지금까찌 몇 일?")
# first_day = datetime.date(2024, 11, 25)
# print(first_day)

# today = datetime.date.today()
# print(today)

# passed_time = today - first_day
# print(passed_time)
# print(f'개강 이후 {passed_time.days}일 지났습니다.')