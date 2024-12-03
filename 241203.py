#for 문
# i = 0
# while i<5:
#     i+=1
#     print(i)
# print("끝")

#continue문
# num = 0
# while num < 10:
#     num = num + 1 
#     if num % 2 == 0:
#         continue 
#     print(num)

#실습1

# n = int(input("어디까지 계산할까요?"))
# sum = 0

# for i in range(1, n + 1):
#     sum += i
# print(f'\n합계: {sum}')

#실습1 번외

# n = int(input("어디까지 계산할까요?"))
# sum = 0

# for i in range(1, n + 1, 2):
#         sum += i
        
# print(f'\n합계: {sum}')

#실습 2

# n = int(input("몇 초?"))
# for i in range(n, 0, -1):
#     print(i, end=' ')
# print('발사!!')

#실습3
# n = int(input("몇 단을 출력할까요?"))

# for i in range(1, 10):
#     print(f"{n} * {i} = {n * i}")

# a = [10, 20, 30]
# print(sum(a))
# print(sum(a)/len(a))
# sum = 0
# for i in a:
#     sum+=1
# print(sum)

# a = [1,2,3,4,5]
# a2=[]
# a3=[]
# a4=[]

# a3 = [i*3 for i in a]
# print(a3)

# a4 = [i*3 for i in a if i%2==0]
# print(a4)

# for y in range(3):
#     for x in range(2):
#         print(f"y:{y}, x{x}")
#     print()

# for i in range(2, 10):
#     print(f'[{i} 단]')
#     for j in range(1, 10):
#         print(f'{i} X {j} = {i*j}')
#     print()

# print('*** 자리배치도 ***')
# customer = int(input('고객수 입력: '))
# row = int(input('좌석열 수 입력: '))

# if customer % row == 0:
#     column = customer // row
# else:
#     column = (customer // row) + 1
# # print(row)

# for i in range(0, row):
#   for j in range(1, column + 1):
#     seat = i * column + j
#     if seat > customer:
#       break
#     print(seat, end=" ")
#   print()

#실습4
# line = int(input("몇 줄?>"))
# for i in range(1, line + 1):
#     print("*"*i)

# line = int(input("몇 줄?>"))
# for i in range(1, line + 1):
#     print(" " * (line - i) + "*" * i)

# line = int(input("몇 줄?>"))
# for i in range(1, line + 1):
#     print(" " * (line - i) + "*" * (2 * i -1))

#실습5

# n = input("숫자 여러 개 입력 : ").split()
# n = [int(num) for num in n]
# print(n)

# max_n = max(n)
# min_n = min(n)

# print(f"가장 큰 값: {max_n}")
# print(f"가장 작은 값: {min_n}")

# total = sum(n) - max_n - min_n
# count = len(n) - 2

# avg = total / count
# print(f"나머지 값의 평균: {avg}")

# # 1 > 실습 5 답안
# input_nums = input('숫자 여러개 입력 > ').split()
# numbers = []
# for n in input_nums:
#     numbers.append(int(n))
# print(numbers)

# # 최대값
# # 1 리스트 평균 구하기
# max_val = numbers[0] #첫번째 값을 최대값으로 설정함
# for i in numbers:  
#     if i > max_val:  # i(요소값)이 max_val 보다 크면
#         max_val = i  # max_val에 i값 저장
        
# # 2 가장 큰/작은 값 구하기
# max_val = max(numbers) # max() 사용
# print("가장 큰 값:", max_val)

# min_val = min(numbers) # max() 사용
# print("가장 작은 값:", min_val)

# # 3 나머지 값의 평균 구하기
# numbers.remove(max_val)
# numbers.remove(min_val)
# # 평균 = 합계 / 개수
# avg = sum(numbers) / len(numbers)
# print("나머지 값의 평균: ", avg)

# list(map) 예시
# a = list(i for i in range(5))
# print(a)
# b = [i for i in range(5)]
# print(b)
# c = list(map(int, ["1","2","3"]))
# print(c)
# c = list(map(int, input().split()))
# e = list(map(str, (1,2,3)))
# print(e)
# d = [i for i in map(int, ["1","2","3"])]
# print(d)