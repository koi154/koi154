# t1 = (10, 20, 30)
# print(type(t1))
# print(t1)
# print(t1[0])
# del t1[0] 안됨
# del t1 가능

# t2 = (10)
# t3 = (10,)
# t4 = 10,20,
# print(type(t4))

# set1 = {1,2,3,3}
# print(set1)
# set2 = set([2,1,3,3])
# print(set2)
# set2.add(4)
# print(set2)
# while len(set2) > 0:
#     a = set2.pop()
#     print(a)
# l1 = [1,2,3,4]
# while len(l1) > 0:
#     a = l1.pop()
#     print(a)

# set3 = set("apple")
# print(set3)
# while len(set3) > 0:
#     a = set3.pop()
#     print(a)

# name = ["1", "2", "3", "2"]
# # a = []
# for i in range(len(name)):
#     if name.count(name[i]) > 1:
#         print(name[i])
#         # name.remove(name[i]) #에러
#         # a.append(name[i])


# name_set = set(name)
# print(name_set)
# name_list = list(name_set)
# name_list.sort()
# print(name_list)

# name = ["1", "2", "3", "2"]
# a = []  # 중복을 제거한 요소를 저장할 리스트

# for i in name:
#     if i not in a:  # 'a' 리스트에 없는 요소만 추가
#         a.append(i)

# print(a)  # 결과 출력

# a = {}
# print(type(a)) #<class 'dict'>
# b = {1} # set()
# print(type(b)) #<class 'set'>
# c = dict()
# c = {1:'a', 'b':'b'}
# print(c) #{1: 'a', 'b': 'b'}
# c[2] = 'c'
# c['c'] = 2
# print(c) #{1: 'a', 'b': 'b', 2: 'c', 'c': 2}
# del c[2]
# del c['b']
# print(c) # {1: 'a', 'c': 2}
# # print(c[2]) error
# print(c.get(2)) #none
# print(c.keys()) # dict_keys([1, 'c'])
# print(c.values()) # dict_values(['a', 2])
# for i in c.keys():
#     print(i, c.get(i)) #1 a c 2

# print('c' in c) #True
# print(2 in c.values()) #True

# dic = {
#     "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
#     "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
#     "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
# }

# print("★ 컴퓨터 사전 ★")
# word = input("검색할 단어를 입력하세요: ")
# if word in dic:
#     print(f'{word}: {dic[word]}')
# else:
#     print("정의된 단어가 없습니다.")

# #실습1. set사용
# inputs = input().split()
# N = int(inputs[0])  
# M = int(inputs[1])      

# # 집합 S 생성
# S = set()  
# for i in range(N):  
#     S.add(input().strip())

# # 검사 문자열 처리
# result = 0  
# for j in range(M):  
#     if input().strip() in S:
#         result += 1

# # 결과 출력
# print(result)

# 실습2. 학생들의 점수를 저장하는 학생 딕셔너리를 생성 
# dict = {"Alice" : 85, "Bob": 90, "Charlie": 95}
# print(dict)

# dict["David"] = 80
# dict["Alice"] = 88
# print(dict)

# del(dict["Bob"])
# print(dict)
# for i in dict:
#     print(f"{i} : {dict[i]}", end = " ")

# d = [
#     [10,20],
#     [30,40],
#     [50,60]
# ]
# d = [
#     [10,20],
#     [30,40],
#     [50,60]
# ]
# print(d)
# print(d[0][0]) #10 
# print(d[0][1]) #20 
# print(d[1][0]) #30
# print(d[1][1]) #40 
# print(d[2][0]) #50 
# print(d[2][1]) #60
# d.append([70,80])
# print(d)
# d[0][0] = 90
# print(d)

# #del(d[1][1])
# print(d)
# print(len(d))
# print(len(d[0]))

# for i in range(0,len(d)):
#     for j in range(0,len(d[i])):
#         print(d[i][j], end=" ")
#     print()

#     for x,y in d:
#         print(x,y)