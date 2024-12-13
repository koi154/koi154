# with open("./output/data.bin", "wb") as f: #wb:쓰기 rb:읽기
#     txt = "안녕"
#     f.write(txt.encode())

# with open("./output/data.bin", 'rb') as f:
#     data = f.read()
#     print(data) #b'\xec\x95\x88\xeb\x85\x95
#     print(data.decode()) #안녕 encode > decode : 인코딩해야지 디코딩 가능

# with open("./output/1.png", 'rb') as f1: #이미지 파일 읽기
#     img = f1.read()
# with open("./output/2.png", 'wb') as f2: #이미지 파일 쓰기
#     f2.write(img)

# try:
#     num = int(input('정수입력'))
# except ValueError:
#     print("장수가 아님!")

# try:
#     num = int(input('정수입력'))
# except ValueError as msg: #오류 내용 (as별칭)
#     print(msg) #시스템이 보내는 예외 메세지 출력 가능

# try:
#     num = int(input('정수입력'))
# except Exception as msg:
#     print(msg)
# else:
#     print("예외없음")

# try:
#     num = int(input('정수입력'))
# except IndexError as msg:
#     print("IndexError",msg)
# except ValueError as msg:
#     print("ValueError",msg)
# except Exception as msg:
#     print("Exception",msg)

# else:
#     print("예외없음")

#다중 예외처리
# try:
#     num = [1,2,3,4]
#     print(who) #예외가 발생할 수 있는 문장(NameError)
#     print(num[3]/0) #예외가 발생할 수 있는 문장(ZeroDivisionError)
#     print(num[100]) #예외가 발생할 수 있는 문장(IndexError)
# except NameError:
#     print("존재하지 않는 변수 호출")
# except IndexError:
#     print("인덱스 에러 발생")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없음!") 
#결과: 존재하지 않는 변수호출  
# => NameError가 먼저 나오므로 IndexError,ZeroDivisionError 오류는 발생하지 않음    
 
#실습. 정수입력 받기 사용자가 저데로 된 정수를 입력할 떄까지 반복하여 입력받기
# while True:
#     try:
#         num = int(input('정수입력: '))
#         print(f"정수 입력 성공:{num}")
#         break

#     except ValueError:
#         print("정수가 아님! 정수를 입력해주세요!")

#finally 구문을 반드시 실행한다.
# while True:
#     try:
#         num = int(input('정수입력: '))
#         break
#     except ValueError:
#         print("정수가 아님! 정수를 입력해주세요!")
#         continue
#     finally:       
#         print("무조건무조건이야:")
        

# print(f"정수 입력 성공:{num}") 

# a=1
# try :
#     a+=1
#     if a > 1:
#         raise Exception # raise하면 무조건 except로 빠진다.
#     a+=2
#     print("a", a)
# except:
#     print("error", a)

class Animal: #부모 클래스
    def breathe(self): #breathe 메서드 
        print("숨을 쉰다") 
    def cry(self): #cry 메서드 :
        raise NotImplementedError # 만약 자식 클래스에서 cry 메서드를 구현하지 않으면 실행 시 NotimplementedErro 발생

class Dog(Animal): #Dog 클래스는 Animal 클래스를 상속받은 자식 클래스입니다.
    def cry(self): # cry 메서드 : 부모 클래스의 cry 메서드를 오버라이드(재정의) 하여 구체적으로 개의 울음소리를 표현한다.
        print("멍멍")
    
d = Dog()
d.breathe()
d.cry()
