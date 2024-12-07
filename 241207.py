# def a(*numbers, b):
#     print(numbers, "b", b)
# # a (1,2,3,4,5) #에러
# a (1,2,3,4, b = 5)

# def b():
#     def c():
#         print("c")
#     c()
# b()

# l = ["p", "y", "t", "h", "o", "n"]
# print("".join(l))

# numbers = [2,1,3,4,1]
# print(len(numbers))

# print (1 if 1<0 else 0)
# print ("abc" if 1<0 else "bcd")

# if 1<0:
#     print("abc")
# else:
#     print("bcd")

# def solution(s):
#     answer = ''
    
#     s = list(s)
#     s.sort()
#     s.reverse()
    
#     for i in s:
#         answer += i
        
#     return answer

# 프로그래머스 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=python3
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     if not answer:
#         answer = [-1]
#     answer.sort()
#     return answer

# 프로그래머스 두 개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))

# 프로그래머스 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# def solution(name, yearning, photo):
#     answer = []
#     for i in photo:
#         score = 0
#         for j in range(len(name)):
#             if name[j] in i:
                
#                 score += yearning[j]
                
#         answer.append(score)
            
#     return answer

# 딕셔너리로 바꾸기
# def solution(name, yearning, photo):
#     answer = []
    
#     # d = {}
#     # for i in range(len(name)):
#     #     d[name[i]] = yearning[i]
#     d = dict(zip(name, yearning))
        
#     for i in photo:
#         sum = 0
#         for j in i:
#             v = d.get(j)
#             if v:
#                 sum += v
#         answer.append(sum)
    
#     return answer


# 프로그래머스 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3
# def solution(x):
#     num = sum(list(map(int,str(x))))
#     if x % num == 0:
#          answer = True
#     else :
#         answer = False
#     return answer

# 프로그래머스 문자열 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3
# def solution(s):
#     answer = ''
    
#     s = list(s)
#     s.sort()
#     s.reverse()
    
#     for i in s:
#         answer += i
        
#     return answer

# 프로그래머스 크기가 작은 부분문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
# def solution(t, p): # t = "3141592" p = "271"
#     answer = 0
#     p_len = len(p) # p="271", p_len = 3
#     p_ = int(p) # "271" > 271

#     for i in range(len(t) - p_len + 1): #len(t)= 7-3+1 =5 5까지 반복(0,1,2,3,4)
#         substring = ""
#         for j in range(p_len): # 3까지 반복(0,1,2)
#             substring += t[i + j] # t[0 = 0+0]=3,t[1]=31,t[2]=314 
#         if int(substring) <= p_: #314 <= 271(0), 141 <=271(1)
#             answer += 1

#     return answer

a = [1,2,3,4]
b = ["a","b","c","d"]
c = list(zip(a,b))
print(c)
d = dict(zip(a,b))
print(d)