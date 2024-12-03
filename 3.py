# print("오늘은 12월 %d일 입니다." % 2)
# print("오늘은 %d월 %d일 입니다." % (12,2))
# print("오늘은 %d%s %d일 입니다." % (12, '월', 2))
# print(f"오늘은 {12}{'월'} {2}일 입니다.")
# print("오늘은 " +str(12)+"월 "+ str(2)+"일 입니다.")
# print("오늘은",12,"월",2, "일 입니다.",sep="")

# print("Hello".upper())
# print("Hello".lower())

# friends = " 고찬국 김다운 김민창"
# a = friends.split("김") # ' '
# print(a)

# sentence = "{}월 {}일" .format(12,2) # 12월 2일
# print(sentence)

# b = "    111    222   "
# print(b.strip())
# print(b.split())
# print(b.lstrip())
# print(b.rstrip())

#실습2
# n1 = input("첫번째 숫자: ")
# n2 = input("두번째 숫자: ")
# n3 = int(n1) * int(n2[2])  # 첫 번째 숫자 × 두 번째 숫자의 1의 자리
# n4 = int(n1) * int(n2[1])  # 첫 번째 숫자 × 두 번째 숫자의 10의 자리
# n5 = int(n1) * int(n2[0])  # 첫 번째 숫자 × 두 번째 숫자의 100의 자리
# n6 = n5 * 100 + n4 * 10 + n3
# print(n3)
# print(n4)
# print(n5)
# print(n6)


# 실습 2 해답
# in1 = int(input())
# in2 = input()

# print(in1*int(in2[2]))
# print(in1*int(in2[1]))
# print(in1*int(in2[0]))
# print(in1*int(in2))

# cart = ["계란", "마늘", "콩나물", "커피"]
# print("두부" in cart)
# print("계란" in cart)

# if 1<3:
#     print("Ture")
#     print("Ture")
# print("False")

# if 1<3:
#     print("Ture")
#     print("Ture")
# print("False")

#실습
# num = int(input())

# if num % 2 != 0:
#     print("홀수")
# if num % 2 == 0:
#     print("짝수")

#실습4
# num = int(input("점수 입력"))
# if num > 89:
#     print("A")
# elif num > 79:
#     print("B")
# elif num > 69:
#     print("C")
# elif num > 59:
#     print("D")
# else:
#     print("E")
# if num > 99:
#     print("만점은 100점입니다.")

#실습5
# age = 75
# int(input("나이를 입력하세요:"))
# method = input("'카드' 또는 '현금'만 입력: ")   

# if age < 8 or age >= 75:
#     fare = "무료"
# elif age < 14:
#     fare = 450 
# elif age < 20:
#     if method == "카드":
#         fare = 720
#     else:
#         fare = 1000
# elif age < 75:
#     if method == "카드":
#         fare = 1200
#     else:
#         fare = 1300
# print(f"{age}세의 {method} 요금은 {fare}입니다.")

#과제1
# n = int(input("정수n을 입력하세요:"))
# num = list(range(1, n + 1))
# odd = num[::2]
# even = num[1::2]

# print(f"전체리스트: {num}")
# print(f"홀수리스트: {odd}")
# print(f"짝수리스트: {even}")

#과제2
# vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
# drink = input("마시고 싶은 음료?: ")

# if drink in vending_machine:
#     print(f"{drink} 드릴게요.")

#과제3
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
user_option = ['1', '소비자', '2', '주인']
user_option = ['1', '추가', '2', '삭제']
print("남은 음료수:", vending_machine)
user = (input("사용자를 종류를 입력하세요: \n1.소비자\n2.주인\n"))


if user == '1' or user == '소비자': #소비자 선택
    drink = input("마시고 싶은 음료? :")
    if drink in vending_machine: # 드링크가 목록에 있으면
        vending_machine.remove(drink) # 목록에 드링크 지우면서 
        print(f"{drink} 드릴게요.")
    else:
        print(f"{drink} 없습니다.")
    print("남은 음료수:", vending_machine)

elif user == '2' or user == '주인': #주인 선택
    action = input("할 일을 선택: \n1. 추가\n2. 삭제\n")
    print("남은 음료수:", vending_machine)
    if action == '1' or action == '추가': #목록 추가
        new_drink = input("추가할 음료수?: ")
        vending_machine.append(new_drink)  # 음료 추가
        vending_machine.sort()
        print(f"추가완료")

    elif action == '2' or action == '삭제': #목록 삭제
        delete_drink = input("삭제할 음료수?: ")
        if delete_drink in vending_machine:
            print("남은 음료수:", vending_machine)
            vending_machine.remove(delete_drink)
            vending_machine.sort()
            print(f"삭제완료.")
        else:
            print(f"{delete_drink}는 지금 없네요.")
    else: 
        print("잘못된 값.")
    print("남은 음료수:", vending_machine)
else:
    print("잘못된 사용자 입력입니다.")