#실습2 supermarket 클래스
# class Supermarket: #클래스 변수, 슈퍼마켓 인스턴스가 생성될 때마다 증가하여 전체 슈퍼마켓의 개수를 저장
#     supermarket_count = 0

#     def __init__(self, location, name, product, customer): #생성자 메서드로, 슈퍼마켓 객체를 초기화
#         self.__location = location 
#         self.__name = name
#         self.__product = product
#         self.__customer = int(customer)
#         Supermarket.supermarket_count += 1 #클래스 변수 증가시켜 인스턴스 생성 개수

#     def print_location(self): #self.__location을 참조하여 위치 정보
#         print(f"위치: {self.__location}") 

#     def change_category(self, new_product): #new_product를 받아 self.__product에 저장
#         self.__product = new_product #new_product를 받아 self.__product에 저장

#     def show_list(self): #현재 판매 중인 물건을 출력
#         print(f"현재 파는 물건: {self.__product} ") #self.__product를 참조하여 정보를 출력

#     def enter_customer(self):
#         self.__customer += 1 #self.__customer 값을 1 증가
        
#     def show_info(self):
#         print(f"가게 이름: {self.__name} ")
#         print(f"위치: {self.__location} ")
#         print(f"파는 물건: {self.__product} ")
#         print(f"손님 수 모두 출력: {self.__customer} ")

#     def show_supermarket_count(self): #생성된 전체 슈퍼마켓 인스턴스의 개수를 출력
#         print(f"슈퍼마켓 클래스 인스턴스 개수: {Supermarket.supermarket_count} ") #클래스 변수 Supermarket.supermarket_count를 참조

# #객체 생성 및 테스트
# sup1 = Supermarket("덕양구", "엘마트", "고기", "4")
# sup1.print_location()
# sup1.show_list()
# sup1.change_category("치킨")
# sup1.show_list()
# sup1.enter_customer()
# sup1.show_info()
# sup1.show_supermarket_count()

# super2 = Supermarket("마포구 도화동", "마켓투", "채소", 15)
# super2.show_info()
# super2.show_supermarket_count()

# 실습2 답안
# class SuperMarket:
#     instance = 0 
#     def __init__(self, location, name, product, customer):
#         SuperMarket.instance+=1
#         self.__location= location # 위치
#         self.__name= name # 가게 이름
#         self.__product= product # 파는 물건
#         self.__customer= customer # 고객의 수

#     def print_location(self):
#         print(f'위치: {self.__location}')

#     def change_category(self, another_product):
#         self.__product = another_product

#     def show_list(self):
#         print(f'상품: {self.__product}')

#     def enter_customer(self):
#         print("손님 입장")
#         self.__customer += 1
#         return self.__customer

#     def show_info(self):
#         print(f'위치: {self.__location}, 이름: {self.__name}, '
#              f'상품: {self.__product}, 고객수: {self.__customer}')
    
#     def show_supermarket_count(self):
#         print("클래스 인스턴스 개수 : ", SuperMarket.instance)
        


# # 테스트
# super1 = SuperMarket("마포구 염리동", "마켓온", "과일", 10)
# super1.print_location()
# super1.change_category("음료")
# super1.show_list()
# super1.enter_customer()  # 고객 들어옴
# super1.enter_customer()
# super1.show_info()
# super1.show_supermarket_count()

# super2 = SuperMarket("마포구 도화동", "마켓투", "채소", 15)
# super2.show_info()
# super2.show_supermarket_count()

# class Country: #부모 클래스
#     def __init__(self):
#         self.name = "나라이름"
#         self.population = "인구"
#         self.capital = "수도"
    
#     def show(self): #메소드
#         print('국가 클래스의 메소드입니다.')
 
# class Korea(Country): #자식 클래스
#     def __init__(self,name):
#         self.name = name
#     def show_name(self):
#         print('국가 이름은: ',self.name)

# country = Korea("대한민국") # Kprea 클래스의 인스턴스 생성
# country.show()
# print(country.name)
# country.show_name()

# class Calculator():
#     def __init__(self):
#         self.value = 100
#     def sub(self,value):
#         self.value -= value

# class MinLimitCalculator(Calculator):
    
#     def sub(self, value):
#         self.value -= value
#         self.value = max(0, self.value)

# cal = MinLimitCalculator()
# cal.sub(20)
# cal.sub(90)

# print(cal.value)

# class Calculator():
#     def __init__(self):
#         self.value = 100

#     def sub(self,value):
#         self.value -= value

#     #파이썬은 매소드 오버로딩 안됨
#     # def sub(self):
#     #     self.value -= 10

#     #파이썬은 매소드 오버로딩 안됨
#     # def sub(self,value1, value2):
#     #     self.value -= value1 - value2

#     def sub(self, *args):
#         self.value = args[0]

# a = Calculator()
# a.sub(10)
# print(a.value)