# import calendar

# calendar.prcal(2024) #2024년 달력 표시
# calendar.prmonth(2024, 12) #2024년 6월 달력 표시
# calendar.weekday(2024, 8 , 12) #날짜에 해당하는 요일 정보



#날짜로 요일 알아내기
# import datetime
# import calendar

# days = ['월', '화', '수', '목', '금', '토', '일']

#오늘의 요일
# weekday = datetime.date.today().weekday()
# print('오늘은 ' + days[weekday] + '요일')
#특정 날짜
# weekday = datetime.date(2025, 12, 25).weekday()
# print( '크리스마스는 ' + days[weekday] + '요일')

#time 모듈

import time

# a = print(time.time()) #현재 시간을 초로 봔한
# time.sleep(2) #2초를 쉬고 출력
# b = print(time.time())
# print(b-a)


# print(time.localtime()) #년,월,일,시,분,초로 반환
# time_str = time.localtime()
# print(time_str.tm_year) #현재 년도 표기

# print(time.ctime()) #날짜와 시간 표기 형태
# print(time.ctime(a))
# print(time.ctime(b))

# 1970.1.1 이후 > UNIX 시스템 시작
# year = round(time.time()/(365*24*60*60)) #round는 소수점 반올림
# day = (time.time()/(24*60*60))

# print(year)
# print(day)

# 수행 시간 측정하기
# start = time.time()
# # 1초 간격으로 출력 0 ~ 10초
# for i in range(10):
#     print(i)
#     time.sleep(1)

# end = time.time()
# print("수행 시간: " + str(end-start) + "초") 

# func 수행시간 측정하기
# def check_time(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(f"수행시간 : {end-start}초")
# def a():
#     for i in range(10):
#             print(i)
#             time.sleep(1)
# def b():
#      for i in range(100):
#             print(i)
#             time.sleep(0.5)

# check_time(a)
# check_time(b)

# f = open("test.txt", "w") #open("파일위치" 'w') w: 파일에 데이터를 쓰기 위해서 연다. 단, 기존의 내영이 모두 사라지고 새로 작성함. w 없으면 read(기본)
# f.write("Hello world\n") # Hello world 쓰기
# f.close()

# f2 = open("test.txt")
# print(f2.read(4)) #4번째까지 출력
# f2.close()

# f3 = open("test.txt", "a") #'a'는 파일의 뒷부분에 데이터를 추가하기 위해 파일을 연다.
# f3.write("Hello world22\n")
# f3.close()

# f2 = open("test.txt")
# print(f2.read()) 
# f2.close()

# f3 = open("test.txt")
# print(f3.readline(), end="") #readline: 한 줄씩 읽어옴.
# print(f3.readline(), end="")
# print(f3.readline(), end="")
# f3.close()