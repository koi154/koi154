# import sys

# print(sys.argv)

# args = sys.argv[1:]
# print(args)
# 터미널에 입력하기:  python sys_ex1.py 123 456 789 

# print(int(sys.argv[1]) + int(sys.argv[2]))
# 터미널에 입력하기:  python sys_ex1.py 123 456

# args = sys.argv[1:] #범위 선택
# print(args) # python 파일명 입력1 입력 2 --- 입력 n

# total = 0 # 0으로 초기화
# for i in args: # 입력한 args 를 i로 변환
#     total += int(i) # i를 계속 더함
# print("합계: ", total)

# args = sys.argv[1:]
# if len(args) <= 2 or len(args) >= 4:
#         #print("Error")
#         sys.exit(0)
# total = 0
# for i in args:
#     if sys.argv[1] == "mul":
#         total = int(sys.argv[2]) * int(sys.argv[3])
#     elif sys.argv[1] == "add":
#         total = int(sys.argv[2]) + int(sys.argv[3])
# print(total)

# import sys

# args = sys.argv
# if (len(args)!=4):
#     print("입력오류")
#     sys.exit(0)
# else :
#     cmd = args[1]
#     num1 = int(args[2])
#     num2 = int(args[3])
#     if cmd == "mul":
#         print(num1*num2)
#     elif cmd == "add":
#         print(num1+num2)

# import os

# os.chdir("C:\\Users\\zer12\\Desktop\\git-test") #디렉터리 경로
# dir = os.popen('git status') # 'dir' 명령으로 열기
# print(dir.read()) #디렉터리 보기(읽기)
# print(os.listdir()) # 파일을 리스트에 저장

# import time
# import random

# word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple', 'grape', 'garlic', 'onion', 'potato'] 

# n = 1 #문제 번호 

# input("[타자 게임] 준비되면 엔터!") 
# start =  time.time() #시작 시간

# while n < 11:
#     print("문제", n) #문제 번호 출력
#     question = random.choice(word) #퀘스쳔을 워드에서 랜덤초이스 초이스는 중복이 가능
#     print(question)
#     user = input() #입력
#     if question == user: #퀘스쳔 = 입력 
#         print("통과!!") 
#         n += 1 # 1씩증가
#     else:
#         print("오타! 다시 도전!")
# end = time.time() #종료 시간
# et = end -start
# print(f'타자 시간: {et: .2f}초') #.2f 소수점 둘째짜리까지 표시