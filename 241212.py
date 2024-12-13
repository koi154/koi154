# f4 = open("test.txt")
# print(f4.readlines()) #readline: 한 줄씩 읽어옴.
# f4.close()

# f5 = open("test.txt", "r+") #'r+' 모드는 읽기와 쓰기 모두 가능한 모드
# print(f5.read()) #파일 내용 읽기
# print(f5.tell()) #커서의 위치를 바이트 
# f5.seek(4) # 5번째 바이트 (0부터 시작)
# print(f5.write("8")) 
# f5.close()

# f6 = open("test.txt", "r+") #'r+' 모드는 읽기와 쓰기 모두 가능한 모드
# str6 = f6.read()
# print(f6.tell()) #파일 내용 읽기
# f6.seek(str6.find('5')) #'5'의 위치를 찾기 seek: 그 위치로 이동
# print(f6.write("8")) # '5'를 8로 바꿈
# f6.close()

# with open("test.txt", "r+") as f7: # with as : f.close() 사용하지 않음.
#     str6 = f7.read()
#     print(f7.tell()) #파일 내용 읽기
#     f7.seek(str6.find('8')) #'5'의 위치를 찾기 seek: 그 위치로 이동
#     print(f7.write("o")) # '5'를 8로 바꿈

# import random
# import time

# with open("word.txt", 'w') as f:
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry', 'grape', 'garlic', 'onion', 'potato']
#     for i in word:
#         f.write(i + ' ')
# # try:
# with open("word.txt", 'r') as f:
# word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry', 'grape', 'garlic', 'onion', 'potato']
# for i in word:
#     # f.write(i + ' ')
#     word = f.read().split()
# # with open("./word.txt", 'r') as f:
#     # data = f.read().split()
#     # word = random.choice(data)
#     # print(word)


# n = 1 #문제 번호
# input("[타자 게임] 준비되면 엔터!")
# start = time.time() #시작 시간

# while n < 11:
#     print("문제", n)
#     question = random.choice(word)
#     print(question) # 문제 출력
#     user = input()
# if question == user:
#     print("통과!!")
#     n += 1
# else:
#     print("오타!! 다시 도전")
# end = time.time()
# print(f"게임 소요 시간: {end-start:.2f}초") #print ("게임을 종료합니다.")

# # except:
# #     print("파일을 찾을 수 없습니다.")

# import random
# import time

# try:
#     with open("word.txt", 'r') as f:
#         word = f.read().split()  # word.txt 파일의 단어들을 리스트로 저장

#     input("타자 게임 준비되면 엔터!!")
#     start = time.time()  # 시작 시간 기록

#     n = 1  # 문제 번호
#     while n < 11:  # 10문제 출제
#         print("문제", n)
#         question = random.choice(word)  # 랜덤하게 단어 선택
#         print(question)  # 문제 출제
#         user = input()  # 사용자 입력
        
#         if question == user:  # 정답이면
#             print("통과!!")
#             n += 1
#         else:  # 오답이면
#             print("오타!! 다시 도전")
        
#         end = time.time()
#         print(f"게임 소요 시간 : {end-start:.2f}초")

# except:
#     print("파일을 찾을 수 없습니다.")


#try - except 대신 사용
# import random
# import time
# import os

# if os.path.exists("word.txt"):
#    with open("word.txt", 'r') as f:
#        word = f.read().split()
# else:
#    word = ['sky', 'earth', 'moon', 'flower', 'tree', 
#            'apple', 'grape', 'garlic', 'onion', 'potato']

# input("타자 게임 준비되면 엔터!!")
# start = time.time()

# n = 1  # 문제 번호
# while n < 11:  # 10문제 출제
#    print("문제", n)
#    question = random.choice(word)  # 랜덤하게 단어 선택
#    print(question)  # 문제 출제
#    user = input()  # 사용자 입력
   
#    if question == user:  # 정답이면
#        print("통과!!")
#        n += 1
#    else:  # 오답이면
#        print("오타!! 다시 도전")
   
#    end = time.time()
#    print(f"게임 소요 시간 : {end-start:.2f}초")

# with open("./output/input.txt", 'a') as f:
#     while True:
#         text = input("저장할 내용 입력(종료-z)")
#         if text == 'z' or text == 'Z':
#             break
#             #sys.exit(0) break 대신 사용 import sys 넣어야함.
#         f.write(text + '\n')

# 실습1. 회원 명부 작성하기
# with open("member.txt", 'w') as f: #member.txt 파일 쓰끼
#     for i in range(3): #3번 반복
#         print(f"{i+1}번째 회원:") #몇 번쨰 회원
#         name = input("이름: ") 
#         pw = input("비번: ")
#         f.write(f"{name} {pw}\n") #이름,비번 파일 저장

# with open("member.txt", "r") as f: #member.txt 읽기
#     print(f.read()) # 파일 모든 내용 읽기

#실습2. 회원 명부를 이용한 로그인 기능
# print("이름을 입력하세요.")
# input_name = input("이름: ") #이름
# print("비밀번호를 입력하세요.")
# input_pw = input("비밀번호: ") #비번

# with open("member.txt", "r") as f: #member.txt 읽기
#     members = f.readlines() # 모든 줄 읽기

#     success = False
#     for member in members:
#         name, pw = member.strip().split() # 이름과 비번 분리
#         if name == input_name and pw == input_pw: #이름 비번 일치하면
#             success = True #성공
#             break
#     if success:
#         print("로그인 성공")
#     else:
#         print("로그인 실패")
        
#dict을 사용한 실습2
# dictUser = {}

# with open("member.txt", 'r') as f:
#     for line in f:
#         n, p = line.split()
#         dictUser[n] = p

# print(dictUser)

# # for i in range(100) :
# name = input("이름을 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")

# if pw == dictUser.get(name):
#     print("로그인 성공!")
# else:
#     print("로그인 실패!")

# 실습3. 로그인 성공 시 전화번호 저장하기.
# print("이름을 입력하세요.")
# input_name = input("이름: ") #이름
# print("비밀번호를 입력하세요.")
# input_pw = input("비밀번호: ") #비번

# with open("member.txt", "r") as f: #member.txt 읽기
#     members = f.readlines() # 모든 줄 읽기

#     success = False
#     for member in members:
#         name, pw = member.strip().split() # 이름과 비번 분리
#         if name == input_name and pw == input_pw: #이름 비번 일치하면
#             success = True #성공
#             break
#     if success:
#         print("로그인 성공")
#         print("전화번호를 입력하세요.")
#         tel = input("전화번호: ") #전화번호 입력

#         tel_exits = False # 전화번호 존재 여부 초기값
#         with open("member_tel.txt", "r") as tel_f: #전화번호 파일 읽기
#             tel_members = tel_f.readlines() # 모든 전화번호 읽기

#             with open("member_tel.txt", "w") as new_tel_f: #전화번호 파일 쓰기
#                 for tel_member in tel_members: # 전화번호 반복문
#                     name_in = tel_members.strip().split() # 이름 불러오오기
#                     if name_in == input_name: # 같은 이름이 있으면
#                         new_tel_f.write(f"{input_name} {tel}\n") # 전화번호 수정
#                         tel_exit =True
#                         print("전화번로를 수정했습니다.")
#                     else:
#                         new_tel_f.write(tel_member) # 다른 사람 번호는 유지

#                 if not tel_exits: # 전화번호가 없다면
#                     new_tel_f.write(f"{input_name} {tel}\n") #새로 추가
#                     print("전화번호를 추가했습니다.")
#     else:
#         print("로그인 실패")

# print("=== 로그인 ===")
# input_name = input("이름: ")
# input_pw = input("비밀번호: ")

# with open("member.txt", "r") as f:
#     members = f.readlines()  # 모든 줄을 읽기

# # 입력된 정보와 파일의 내용 비교
# success = False
# for member in members:
#     name, pw = member.strip().split()
#     if name == input_name and pw == input_pw:
#         success = True
#         break

# if success:  # 로그인 성공하면
#     print("로그인 성공!")
#     print("전화번호를 입력하세요.")
#     tel = input("전화번호: ")
    
#     try:
#         # member_tel.txt 확인
#         with open("member_tel.txt", "r") as f:
#             tel_data = f.read()
            
#         if input_name in tel_data:  # 이미 전화번호가 있으면
#             print("전화번호를 수정했습니다.")
#         else:  # 새로운 사용자면
#             print("전화번호를 추가했습니다.")
            
#         # 전화번호 저장/수정
#         with open("member_tel.txt", "w") as f:
#             f.write(f"{input_name} {tel}\n")
            
#     except FileNotFoundError:  # 파일이 없으면
#         with open("member_tel.txt", "w") as f:
#             f.write(f"{input_name} {tel}\n")
#         print("전화번호를 추가했습니다.")
        
# else:
#     print("로그인 실패")


# dict을 사용한 실습2
# import os
# dictUser = {}

# with open("member.txt", 'r') as f:
#     for line in f: #파일의 각 줄 읽음
#         n, p = line.split() # n,p로 분리
#         dictUser[n] = p # 이름이 키, 비번이 값

# name = input("이름을 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")

# if pw == dictUser.get(name): #입력한 비번이 저장된 비번가 일치확인 get(name) : 값(비번)
#     print("로그인 성공!")
#     tel = input("전화번호를 입력하ㅔ요: ") #전화번호 입력
#     tel_dict = {} #전화번호 딕셔너리 생성

    
#     if os.path.exists("member_tel.txt"): #member_tel.txt 파일 있으면
#         with open("member_tel.txt", 'r') as f:
#             for line in f: #파일 각 줄 읽음
#                 n, t = line.split() # 이름(n)과 전화번호 (t) 분리
#                 tel_dict[n] = t # 이름이 키, 전화번호 값을 딕셔ㅓ리로 저장
    
#     is_new = name not in tel_dict #tel_dict에 이름 없으면 True
#     tel_dict[name] = tel # 전화번호 저장/수정
    
#     with open("member_tel.txt", 'w') as f:
#         for n, t in tel_dict.items(): #딕셔너리의 모든 항목을
#             f.write(f"{n} {t}\n")  # 파일에 저장
    
#     # 결과 출력
#     if is_new:
#         print("전화번호를 추가했습니다.")
#     else:
#         print("전화번호를 수정했습니다.")
# else:
#     print("로그인 실패!")

# 실습 3

# import sys

# def successLogin(name, pw):
#     dictUser = {}
#     with open("member.txt", 'r') as f:
#         for line in f:
#             n, p = line.split()
#             dictUser[n] = p

#     print(dictUser)

#     return pw == dictUser.get(name)
    
# name = input("이름을 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")
    
# if not successLogin(name, pw):
#     print("로그인 실패")
#     sys.exit(0)

# print("로그인 성공")
# phone = input("전화번호를 입력하세요.: ")

# with open("member_tel.txt", "r") as f:
#     m_tel_list = f.readlines()
#     print(m_tel_list)

# user_tel = name + " " + phone + "\n"

# with open("member_tel.txt", "w") as f:
#     write = False
#     for i in m_tel_list:
#         if i.split()[0] == name:
#             f.write(user_tel)
#             write = True
#         else :
#             f.write(i)
#     if not write:
#         print("not write", user_tel)
#         f.write(user_tel)