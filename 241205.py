# d = [
#     [3,1],
#     [3,2],
#     [3,3],
#     [3,4],
#     [3,5],
#     [3,6],
#     [3,7],
#     [3,8],
#     [3,9],

# ]

# for x,y in d:
#     print(f"{x} * {y} = {x*y}")

# for i in d:
#     print(f"{i[0]} * {i[1]} = {i[0]*i[1]}")

# def f(x):
#     result = x**2 + 2*x + 1
#     return result

# print(f(3))

# def sayHi():
#     print("Hi")
#     print("Hi")
#     print("Hi")

# sayHi()

# def say_hello(n): # f(x) 
#     for i in range(n): 
#         print("hello") 
# say_hello(3) # f(3)

# x = 10

# def func2():
#     print("func2", x)
#     # print(y)

# def func():
#     x = 20
#     y = 11
#     print("func",x, y)
#     func2()

# func()
# print("main", x)
# # print("main", y)

# func2()

# def func3(x):
#     print("func3", x)

# func3(3)


#실습1
# def num(n,m):
#     if n == m:
#         return n * m
#     else:
#         return n + m
# result1 = num(2,2)
# result2 = num(2,3)

# print("결과(곱):", result1)
# print("결과(합):", result2)


#실습2 
# def price(x,y):
#     if x * y < 20000:
#         return  x * y + 2500 
#     else:
#         return  x * y 
# result1 = price(15000,2)
# result2 = price(15000,1)

#실습2 답안
# print("상품1 가격:", result1)
# print("상품2 가격:", result2)

# def get_price(price, quantity):
#     order_price = price * quantity
#     fee = 2500
#     if order_price < 20000:
#         order_price += fee
#     return order_price
# print(f'상품1 결제: {get_price(15000,2)}원')
# print(f'상품2 결제: {get_price(5000,3)}원')


#리스트를 매개변수로 새로운 리스트 만들기
# def times(l): 
#     l2 = [ i * 2 for i in l]
#     return set(l2)

# v2 = times([1,2,3,4,5,])
# print(v2)

# 두 개 return
# def sum_mul(a,b):
#     sum = a+b
#     mul = a*b
#     return sum,mul
# s, m = sum_mul(2,3)
# print(s,m)


#실습3. 자판기 프로그램 함수화

# vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

# def check_machine(): #남는 음료수
#     print("남은 음료수:", vending_machine)
          
# def is_drink(drink): #음료수 확인
#     return drink in vending_machine

# def add_drink(): #음료수 추가
#     new_drink = input("추가할 음료수?: ")
#     vending_machine.append(new_drink)
#     vending_machine.sort()
#     print(f"{new_drink} 추가 완료.")

# def remove_drink(drink): #음료수 제거
#     delete_drink = input("삭제할 음료수?: ")
#     if is_drink(delete_drink):
#         vending_machine.remove(delete_drink)
#         print(f"{delete_drink} 삭제 완료.")
#     else:
#         print(f"{delete_drink}는 현재 목록에 없습니다.")

# def vending_machine_program(): #자판기 프로그램
#     check_machine() #남는 음료수
#     user = input("사용자 종류를 입력하세요: \n1. 소비자\n2. 주인\n")
#     if user == '1':
#         consumer_mode() #고객모드
#     elif user == '2':
#         owner_mode() #주인모드
#     else:
#         print("잘못된 사용자 입력입니다.")

# def consumer_mode(): #고객 모드
#     drink = input("마시고 싶은 음료?: ")
#     if is_drink(drink):
#         vending_machine.remove(drink)
#         print(f"{drink} 드릴게요.")
#     else:
#         print(f"{drink}는 없습니다.")
#     check_machine() #남는 음료수

# def owner_mode(): #주인 모드
#     action = input("할 일을 선택: \n1. 추가\n2. 삭제\n")
#     if action == '1':
#         add_drink()
#     elif action == '2':
#         remove_drink()
#     else:
#         print("잘못된 입력입니다.")
#     check_machine() #남는 음료수

# vending_machine_program() #자판기 프로그램


# 실습3 답안
# vending_machine = ['게토레이', '게토레이', '레쓰비', '생수', '이프로']

# def check_machine():
#     print("남은 음료수: ", vending_machine)

# def is_drink(vending_machine, drink):
#     return drink in vending_machine

# def add_drink(vending_machine, drink):
#     vending_machine.append(drink)
#     vending_machine.sort()

# def remove_drink(vending_machine, drink):
#     vending_machine.remove(drink)

# while(1):
#     who = int(input("사용자 종류를 입력하세요(1.소비자, 2.주인) : "))
#     if who == 1:
#         drink = input("마시고 싶은 음료? ")
#         if is_drink(vending_machine, drink):
#             print(drink, "드릴게요")
#             remove_drink(vending_machine, drink)
#             check_machine()
#         else:
#             print(f"{drink}는 지금 없네요")
#     else:
#         todo = int(input("할 일 선택(1.추가, 2.삭제) : "))
#         if todo == 1:
#             print("남은 음료수: ", vending_machine)
#             drink = input("추가할 음료수? ")
#             add_drink(vending_machine, drink)
#             print("추가 완료")
#             print("남은 음료수: ", vending_machine)
#         else:
#             print("남은 음료수: ", vending_machine)
#             drink = input("삭제할 음료수? ")
#             if is_drink(vending_machine, drink):
#                 remove_drink(vending_machine, drink)
#                 print("삭제 완료")
#                 print("남은 음료수: ", vending_machine)
#             else:
#                 print(f"{drink}는 지금 없네요")

# 실습3 refactor 사용하기
# vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
# user_option = ['1', '소비자', '2', '주인']
# user_option = ['1', '추가', '2', '삭제']
# print("남은 음료수:", vending_machine)
# user = (input("사용자를 종류를 입력하세요: \n1.소비자\n2.주인\n"))


# def check_machine(vending_machine):
#     print("남은 음료수:", vending_machine)

# def add_drink(vending_machine, new_drink):
#     vending_machine.append(new_drink)  # 음료 추가
#     vending_machine.sort()

# def remove_drink(vending_machine, delete_drink):
#     vending_machine.remove(delete_drink)

# if user == '1' or user == '소비자': #소비자 선택
#     drink = input("마시고 싶은 음료? :")
#     if drink in vending_machine: # 드링크가 목록에 있으면
#         vending_machine.remove(drink) # 목록에 드링크 지우면서 
#         print(f"{drink} 드릴게요.")
#     else:
#         print(f"{drink} 없습니다.")
#     check_machine(vending_machine)

# elif user == '2' or user == '주인': #주인 선택
#     action = input("할 일을 선택: \n1. 추가\n2. 삭제\n")
#     check_machine(vending_machine)
#     if action == '1' or action == '추가': #목록 추가
#         new_drink = input("추가할 음료수?: ")
#         add_drink(vending_machine, new_drink)
#         print(f"추가완료")

#     elif action == '2' or action == '삭제': #목록 삭제
#         delete_drink = input("삭제할 음료수?: ")
#         if delete_drink in vending_machine:
#             check_machine(vending_machine)
#             remove_drink(vending_machine, delete_drink)
#             print(f"삭제완료.")
#         else:
#             print(f"{delete_drink}는 지금 없네요.")
#     else: 
#         print("잘못된 값.")
#     check_machine(vending_machine)
# else:
#     print("잘못된 사용자 입력입니다.")


# 실습4
# import sys

# def stack_program():
#     input = sys.stdin.readline
#     n = int(input().strip())
#     stack = []

#     for _ in range(n):
#         command = input().strip().split()  # 공백으로 명령어를 나눔
#         if command[0] == "push": # 추가만 함 (출력X)
#             stack.append(int(command[1]))  # 숫자를 스택에 추가
#         elif command[0] == "pop": # 스택에서 가장 위에 정수 빼고, 정수 출력 / 만약 정수가 없는 경우 -1 출력
#             print(stack.pop() if stack else -1)
#         elif command[0] == "size": # 스택에 들어있는 정수의 개수 출력
#             print(len(stack))
#         elif command[0] == "empty": # 스택이 비어있으면 1, 아니면 0을 출력
#             print(1 if not stack else 0)
#         elif command[0] == "top": # 스택의 가장 위에 정수 출력 / 만약 정수가 없는 경우 -1 출력
#             print(stack[-1] if stack else -1)

# 프로그램 실행
# stack_program()



# # 실습4
# import sys
# # 스택을 전역 변수로 선언
# stack = []
# # push 함수
# def push(x): # 추가만 함 (출력X)
#     stack.append(x)
# # pop 함수
# def pop(): # 스택에서 가장 위에 정수 빼고, 정수 출력 / 만약 정수가 없는 경우 -1 출력
#     if stack:
#         print(stack.pop())
#     else:
#         print(-1)
# # size 함수
# def size(): # 스택에 들어있는 정수의 개수 출력
#     print(len(stack))
# # empty 함수
# def empty(): # 스택이 비어있으면 1, 아니면 0을 출력
#     print(1 if not stack else 0)
# # top 함수
# def top(): # 스택의 가장 위에 정수 출력 / 만약 정수가 없는 경우 -1 출력
#     if stack: 
#         print(stack[-1])
#     else:
#         print(-1)
# # 메인 함수
# def stack_program():
#     input = sys.stdin.readline
#     n = int(input().strip())  # 명령어의 수

#     for _ in range(n):
#         command = input().strip().split()  # 명령어를 공백으로 나눔
#         # cmd = command[0]
#         # if cmd == "push":
#         #     push(int(command[1]))
#         # elif cmd == "pop":
#         #     pop()
#         # elif cmd == "size":
#         #     size()
#         # elif cmd == "empty":
#         #     empty()
#         # elif cmd == "top":
#         #     top()
#         match command[0]:
#             case "push":
#                 push(int(command[1]))
#             case "pop":
#                 pop()
#             case "size":
#                 size()
#             case "empty":
#                 empty()
#             case "top":
#                 top()

# # 프로그램 실행
# stack_program()

# def oneup():
#     global x
#     x = x + 1
#     return x

# x = 0 
# print(oneup())
# print(oneup())
# print(oneup())  

#실습5

# def get_times(n):
#     global count
#     for i in range(1,31):
#         if i % n == 0:
#             print(i, end=" ")
#             count += 1

# n = 3
# count = 0
# get_times(n)
# print(f'\n{n}의 배수의 개수: {count}')

#실습5 #global 빼기

def get_times(n):
   
    for i in range(1,31):
        if i % n == 0:
            print(i, end=" ")
            count += 1

n = 3
count = 0
get_times(n)
print(f'\n{n}의 배수의 개수: {count}')