"""
print(3//2)
print(3.25//2)
print(3%2)
print(3.25%2)
print(2**3)
print(2**10)

#연산자 우선순위
print(1+2*3**2)
print(1+(2*(3**2)))
print(1+2*-3**2)
print(1+2*(-3)**2)

#몫과 나머지 계산하기
bread = 30
people = 4

bread_count = bread // people
remaining_bread = bread % people

print(f"빵의 개수 = {bread_count} 남은 빵의 개수 = {remaining_bread}")

a = 1
a += 1 # a = a+1
print(a)

print("장원영"+" 럭키비키")
print("럭키"*10)
# print("럭키"*"비키") #에러


#입력: input()
song = input("너의 최애 노래는?")
print(song)
print(type(song))

#형변환
a = input("1+1=?")
#print(a)
print(int(a)*2)
"""

#한번에 정수/실수형 변환
#number = int(input())
#ff = float(input())

#a = 2
#print(str(2)*10)
#print(str(2)+"입니다.")
# print(2+"입니다") #에러

#실습2
#print("|\_/|")
#print("q p  /}")
#print('( 0 )"""\\')
#print('|\"^\"\'    |')
#rint('||_/=\\\\__|')

#실습3
#name = input("이름을 입력하세요.")
#age = input("나이를 입력하세요.")
#print(f"안녕하세요! {name}님 ({age}세)")

#name = input("이름을 입력하세요. ")
#birth_year = int(input("태어난 년도를 입력하세요. "))
#current_year = int(input("올해 년도를 입력하세요. "))

#age = current_year - birth_year + 1
#print(f"올해는 {current_year}년, {name}님의 나이는 {age}세 입니다.")

a = []
b = [1,2,3,4]
c = ["장원영", "안유진"]
d = [1, "아이브"]

# print(len(c))
# print(c[0])
# print(c[1])
# c[0] = "카리나"
# print(c)
# del c[0]
# print(c)
# del c[0]
# print(c)
# c.append("asdfs")
# print(c)

# print(b[-1])
# print(b[-2])
# print(type(b))

# seasons = ["봄", "여름", "가을", "겨울"]
# print(seasons[0:1])
# print(seasons[0:2])
# print(seasons[:2])
# print(seasons[1:])
# print(seasons[2:])
# print(seasons[1:3])
# print(seasons[:])
# print(seasons[::3])
# print(seasons[::-1])

# seasons2 = ["봄", "여름", "가을", "겨울", [1,2,3,4]]
# print(seasons2[-1][0])

# abc = "abc"
# abcd = ['a','b','c']
# print(len(abc))
# print(len(abcd))

# a = [1,2,3,4,5,6,7,8,9,10]
# even = a #a를 이용해서 짝수만 뽑은 리스트 만들기
# print(a[1:10:2])

# a = [3,4,2,1]
#a.sort()
#a.sort(reverse=True)
# a.reverse() #a[::-1]
# print(a)

# b = ["a","b","c","d"]
# b.sort()
# print(b)

# c = ["1","10","11","2"]
# c.sort()
# print(c) # 1,10,11,2 이 str이여서

# d = ["강남","강북", "서", "서","서"]
# d.sort()
# print(d)

# first = d.index("서")+1
# print(first +d[first+1:].index("서")) # 두번째 서
# print(d.count("서"))

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[2])
rainbow.sort()
print(rainbow)
rainbow.append("pink")
print(rainbow)
del rainbow[3:7]
print(rainbow)

shop = ["반팔", "청바지", "이어폰", "키보드"]

shop.pop(1)
print(shop) #['반팔', '이어폰', '키보드']
shop.pop()
print(shop) #['반팔', '이어폰']

a = ["a", "b", "c", "b"]
print(a.count("b")) # 2