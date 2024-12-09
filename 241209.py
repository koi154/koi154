# 콜라츠 수열 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/181919
# def solution(n):
#     answer = []
#     def collat(x):
#         answer.append(x)
#         if x == 1 :
#             return
#         elif x%2==0:
#             collat(x/2)
#         else : 
#             collat(x*3+1)
    
#     collat(n)
#     return answer

# 특이한 정렬 https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3
# def solution(numlist, n):
#     answer = []
#     d = {}
#     for i in numlist:
#         d[i] = abs(i-n)
#     d1 = sorted(d.items(), key= lambda item:(item[1], -item[0]))
#     print(d.items())
#     print(d1)
    
#     for i in d1:
#         answer.append(i[0])
        
#     return answer

# 옹알이(1) https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3
# def solution(babbling):
#     answer = 0
    
#     can = ["aya", "ye", "woo", "ma"]
    
#     for i in babbling:
#         for j in can:
#             idx = i.find(j)
#             if idx > -1:
#                 print(idx,i,j)
#                 i = i.replace(j, '_')
#                 print(idx, i , j)
#         i = i.replace('_', '')
#         if len(i) == 0:
#             answer+=1
            
#     return answer

#하노이의 탑 https://school.programmers.co.kr/learn/courses/30/lessons/12946
# def solution(n):
#     answer = []
    
#     def hanoi(n, f, t, v):
#         if n == 1:
#             answer.append([f,t])
#         else:
#             hanoi(n-1, f,v,t)
#             answer.append([f,t])
#             hanoi(n-1, v,t,f)
            
#     hanoi(n, 1, 3, 2)
        
#     return answer

# a = dict()
# a = set()

# class b:
#     pass

# bb = b()
# bb2 = b()
# bb3 = b()

# 클래스 변수 (필드,Field)
# class Movie:
#     title = "범죄도시4"

# movie1 = Movie()
# movie2 = Movie()

# print(movie1.title)
# print(movie2.title)

# movie1.title = "파묘"
# print(movie1.title)
# print(movie2.title)

# movie1.score = "1"
# print(movie1.score)
# print(movie2.score) > erro movie1 만 바꿔서


# 클래스 함수(메소드,Method)
# class Movie:
#     name = ''

#     def print_msg(msg) : 
#         print(msg)
#     def modify(self, movie):
#         self.name = movie
#     def print_name(self):
#         print(self.name)

# movie1 = Movie()
# movie2 = Movie()

# Movie.print_msg("print하기")
# Movie.modify(movie1, "print하기2")
# movie1.modify("프린트하기3")
# movie1.print_name()
# movie2.modify("프린트하기4")
# print("movie2.name", movie2.name)

# 생성자
# class Movie:
#     def __init__(self):
#         print("Hello")

# moive = Movie()

# 매개변수가 있는 생성자
# class Movie:
#     count = 0

#     def __init__(self, title , audience ):
#         self.title = title
#         self.audience = audience

# movie1 = Movie("파묘", 100)
# movie2 = Movie("파묘2", 200)

# print(movie1.title, movie1.audience)
# print(movie2.title, movie2.audience)

# class Movie:
#     count = 0
#     def __init__(self, title, audience):
#         self.title = title
#         self.audience = audience
#         Movie.count += 1

# movie1 = Movie("파묘", 100)
# print(Movie.count) #1
# movie2 = Movie("파묘2", 200)

# print(movie1.count) #2
# print(movie2.count) #2
# print(Movie.count) #2

# print(movie1.count) #2
# print(movie2.count) #2
# print(Movie.count) #2
# Movie.count += 1
# print(movie1.count) #3
# print(movie2.count) #3
# print(Movie.count) #3
# movie1.count += 1
# print(movie1.count) #4
# print(movie2.count) #3
# print(Movie.count) #3

# class Movie:
#     count = 0
#     def __init__(self, title, audience):
#         self.__title = title
#         self._audience = audience
#         Movie.count += 1
    
#     def get_title(self): # 외부유입 가능
#         return self.__title
    
#     # def set_title(self,title):
#     #     self.__title = title # 내부조건

#     def get_audience(self):
#         return self._audience

# movie1 = Movie("파묘", 100)
# # print(movie1.__title)
# print(movie1.get_title())
# # movie1.__title = "오겜"
# # print(movie1.get_title())
# # print(movie1.__title)
# print(movie1._audience)
# print(movie1.get_audience())

# class MyAdd:
#     __a = 1 # 프라이빗 클래스, 클래스 내부에서만 접근 
#     __b = 2 # 프라이빗 클래스, 클래스 내부에서만 접근

#     def sum(self):
#         return self.__a + self.__b # __a와 __b 값을 사용
#     def set_a(self,a):
#         self.__a = a # 외부에서 __a값을 변경할 수 있도록 제공
    
# a = MyAdd() # 초기값 __a = 1, __b = 2
# print(a.sum()) # 3

# a.set_a(3) # __a 값을 3으로 변경
# print(a.sum()) # 5

# class Health:
#     def __init__(self, name):
#         self.__name = name
#         self.__hp = 100

#     def getName(self):
#         return self.__name
    
#     def setHp(self, hp):
#         hp = max(hp, 0)
#         hp = min(hp, 100)
#         self.__hp = hp

#     def getHp(self):
#         return "hp: " + str(self.__hp)
    
#     def exercise(self, hours):
#         self.setHp(self.__hp + hours)
#         print(f"{hours}시간 운동하다")

#     def drink(self, cups):
#         self.setHp(self.__hp - cups)
#         print(f"술을 {cups}잔 마시다")

# p1 = Health("나몸짱")
# p1.setHp(100)
# p1.exercise(5)
# p1.drink(2)
# print(f"{p1.getName()} - {p1.getHp()}")

# p2 = Health("나약해")
# p2.setHp(10)
# p2.exercise(1)
# p2.drink(12)
# print(f"{p2.getName()} - {p2.getHp()}")

# class math:
#     def __init__(self, a, b):  #입력받은 두 숫자 a,b를 프라이빗 변수로 저장
#         self.__a = a
#         self.__b = b

#     def add(self): #__a와 __b를 더한 결과
#         return self.__a + self.__b
#     def sub(self): #__a와 __b를 뺀 결과
#         return self.__a - self.__b
#     def mul(self): #__a와 __b를 곱한 결과
#         return self.__a * self.__b
#     def div(self): #__b가 0이라면 0으로 나눌 수 없으므로 None
#         if self.__b==0:
#             return None
#         else:
#             return self.__a / self.__b
# math1 = math(4,0)

# print(math1.add())
# print(math1.sub())
# print(math1.mul())
# print(math1.div())

# class Employee:
#     serial_num = 1000

#     def __init__(self,name):
#         Employee.serial_num += 1
#         self.id = Employee.serial_num
#         self.name = name
    
#     def __str__(self):
#         return f"사번 : {self.id}, 이름 : {self.name}"

# e1 = Employee("최사원")
# print(e1)
# e2 = Employee("안사원")
# print(e2)
# e3 = Employee("한사원")
# print(e3)


# employee = [
#     Employee('구름'),
#     Employee('별'),
#     Employee('행성'),
#     Employee('달')
# ]

# for i in employee:
#     print(i) # 둘 중 한개 

# print("\n".join(map(str, employee))) # 둘 중 한개 