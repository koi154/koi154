# def pr_str(txt, count=1, count2=1):
#     for i in range(count):
#         print(txt)
#         print(count2)

# pr_str("Hello", 3, 2)
# pr_str("Hello", 3)
# print()
# pr_str("Hello")
# print()
# # pr_str() #txt='12'
# def calc_avg(*numbers):
#     print(type(numbers))
#     return sum(numbers)/len(numbers)
# print(calc_avg(1,2))
# print(calc_avg(1,2,3,4,5))

# def a():
#     return 1,2

# print(a())

# def intro(**kw):
#     print(type(kw))
#     for k, v in kw.items():
#         print(f"{k}: {v}")
#     for i in kw:
#         print(f"{i}")
# intro(name="Alice", age=25, city="NY")

# list = [2,4,1,4,6]
# list.sort() #sort()는 리스트를 제자리에서 정렬하고, 원본 데이터를 변경합니다.
# print("list",list)
# list2 = [2,4,1,4,6]
# print("sorted list2",sorted(list2)) #sorted()는 원본 데이터를 변경하지 않고, 정렬된 새로운 리스트를 반환합니다.
# print("list2",list2)

# 3번쨰로 작은 값의 인덱스를 구하라
# 정렬하고 그 값을 원본에서 찾으면 된다.

# print(eval("1+2*2"))
# print(int(4.6+0.5))
# print(int(4.4+0.5))
# print(round(4.4))
# print(round(4.5))

# print(round(2.547))
# print(round(2.547, 1))
# print(round(2.547, 2))
# print(round(127, -1))
# print(round(127, -2))
# print(round(127))

# sum_v1 = sum([1,2,3,4])
# print("sum_v1 =", sum_v1)

# print(2**3)
# print(pow(2,3))

# def hello():
#     global x
#     x += 1
#     if x<4:
#         print("hello") 
#         hello()
# x = 0
# hello()

# n = 5
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

#실습2. 재귀함수로 피보나치 수열 구하기
# def fibonacci(n):
#     # if n == 1 or n == 2:
#     if n <= 2:
#         return 1
#     return fibonacci(n-2) + fibonacci(n-1)
# for i in range(1, 10):
#     print(f"F({i}) = {fibonacci(i)}")

# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))

# 방법2
# memory = {1: 1, 2: 1}

# def fibo_memoization(n):
#     if n in memory:
#         number = memory[n]
#     else:
#         number = fibo_memoization(n-1) + fibo_memoization(n-2)
#         memory[n] = number
#     return number

# for i in range(1, 100):  # 원하는 범위 지정
#     print(f"F({i}) = {fibo_memoization(i)}")

# add = lambda x,y:x+y
# print(type(add))
# print(add(1,2))

# def add2(x,y):
#     return x+y
# add3 = add2
# print(add2(1,2))
# print(add3(1,2))

# def call_3(func):
#     for i in range(3): #3번 실행 > for 루프를 통해 func()가 3번 호출
#         func() # func = 매개변수

# call_3(lambda:print("hi"))
# call_3(lambda:print("helllo"))

# def download(startCallback, endedCallback) :
#     startCallback()
#     print("download 중")
#     # download
#     ###
#     ###
#     endedCallback()

# download(lambda:print("다운로드 시작"), lambda:print("완료되었습니다."))

# list(map(int,["1","2","3"]))

# result = map(lambda x:3*x, [1,2,3,4])
# print(list(result))

# l1 = [-5,1,2,-11,76]

# Value = list(filter(lambda x : x<0, l1))
# print(Value) #[-5, -11]
 
# Value = list(filter(lambda x : x>10, l1))
# print(Value) #[76]

# Value = list(filter(lambda x : x >= 3, map(lambda x : 2 * x, l1 )))
# print(Value)

