# day1, day2

# Type: 언어가 처리할 수 있는 데이터(값)의 종류
# 숫자, 문자(열), 참거짓등이 있다.

# 숫자 (int, float)
# int는 정수, float은 실수
print(3+5)
print(10-5)

# 문자열 (str)
# '나 "로 감싼다
print('')  # 얘도 문자열임(빈 문자열)
print('3+5')
print('10-5')
print('python')
print("python")

# "python" or 'python'을 출력하고 싶으면
print('"python"')
print("'python'")

# '''or """로 감싸면 줄을 바꿀 수 있는 문자열 또는 여러줄 주석으로 사용
'''
파이썬 
수업진도 복습할때 나도코딩 참고, 
예제는 파이썬 300제 참고
'''
print('''python 
      
         파이썬''')
print("""python""")
print('''Hello World''')
print("Mary's coffee")
print('"도둑이야"')

# f-문자열 (문자열 안에 변수가 들어간 형태)
'''
name = input('이름 입력: ')
print('이름은 name')
print(f'이름은 {name}')
print(f"이름은 {name}")
your_hobby = input('취미: ')
print(f'당신의 취미는 {your_hobby}')
'''

# 타입을 확인할 수 있는 방법 >> type함수
print(3)
print('3')
type(3)
type('3')

print(type('ㅎㅇ'))
print(type("ㅎㅇ"))
print(type("""ㅎㅇ"""))
print(type('3'))
print(type(3))
print(type(3.14))

# None을 저장하면 NoneType이 나온다
a = None
print(type(a))

# 숫자타입
# 1. int 정수
# 2. float 실수

# 문자타입 str
# 사용자에게 입력받은 값의 타입은 모두 문자열이다. (키보드로 입력받으면 모두 문자열(str).)
# 개발자가 타입을 바꿔준다. -> 밑에서 계속

# 참거짓 bool
print(True)
print(False)

print(type(True))
print(type(False))

# 참거짓연산(논리연산): not, and, or ...
# 논리부정 not (True를 False로 False를 True로)
print(not True)
print(not False)
print(not 5 > 3)

# 파이썬에서 논리연산(참거짓연산)을 사용하면 0은 거짓, 0이 아니면 참
print(5)  # 5가 나옴 => 5는 참도 거짓도 아님
print(not 5)  # not 붙이니까 파이썬에서 5의 타입을 참거짓으로 바꿈

print(not 0)  # 이럴때 숫자는 다 참인데 0은 거짓
print(0 == True)

# 파이썬에서 논리부정을 사용하면 ''은 거짓, 채워진 문자열은 참
# 비교연산은 성립하지 않음 => 다 False로 뜬다
print(not '')
print(not 'ㅇㅇㅇ')
# print('' == True)
# print('' == False)

# 결론: 파이썬에서 타입은 고정된 것이 아니라 바뀔 수 있다.

# -----------------------------------------------------------------------------------------------
# 파이썬은 타입을 바꿀 수 있고 파이썬이 알아서 바꾸는 경우도 있다.
# 파이썬이 알아서 바꾸는 것보다 내가 바꾸는 코드가 더 좋은 코드임.

# 타입을 바꾸는 함수는 타입의 이름과 같다
int('3')  # 문자 3을 숫자 3으로
print(int('3'))
print(type(int('3')))

print(3 + int('3'))
print(3 + float('3.14'))  # 실수는 근사값이다. >> 6.14로 딱 떨어져서 나오지 않음

print('5' + str(5))

print('당신은 성인입니까? ' + str(True))
# 생각보다 까다롭기 때문에 내가 타입을 바꿔주는게 좋음

# 타입 (언어에서 사용되는 데이터의 종류.(어떤 언어의 재료들) 언어마다 조금씩 다름):
# in Python
# 값 1개짜리 타입: int, float, str, bool
# 값 여러개 타입: list-[2,3,4], dictionary-{"name":홍길동, "age":20}, tuple, set
# list는 값들이 서로 상관없이 나열만 된거고, dictionary는 값들이 서로 연관이 있음

# -----------------------------------------------------------------------------------------------
# day3

# 기본 type (순정상태에서 사용할 수 있는 타입 = 원래부터 있는 타입)
# ex)  자바스크립트  : 문자열(string) 숫자(number) 참거짓(bool)
#      오라클       : 문자열(char), 숫자(number), 날짜(date)
#      파이썬       : 문자열(str) 숫자(int, float) 참거짓(bool)

# 파이썬에서 날짜를 쓰고 싶으면 확장하면 된다. (모듈로 확장함)
# 처음 파이썬 깔면 모듈도 같이 깔리긴 하는데 읽어오진 않음 => import로 불러오면 됨
# ex) import datetime

# -----------------------------------------------------------------------------------------------
# literal (코드에 값이 직접 나타나는 것, 값을 직접 적어 놓는 것)
# ex) 3, 3.14, a=60, b=30
# 코드에 literal이 적은게 좋은 코드
# input으로 받는 것들도 input을 받기 전 그냥 임의로 5, 10 이런식으로 정해두면 이건 literal

# day2 입출력연습 예제에서는 60, 30같은게 literal임.
# 근데 여기서 60 ,30은 리터럴이자 상수(변하지 않는 값) 1분=60초

# 상수 = 꼭 있어야만 하는 literal
# 상수는 대문자로
# ex) SECONDS_PER_MINUTE = 60

#
#
# day5
# primitive type - 원시타입. 그냥 처음부터 있는 타입 (사람으로 치면 친부인권)
# 값1개, 복합타입(sequence type)
# 값1개 - int float str bool
# sequence - list tuple set dictionary(자바에선 map)


# CRUD (Create, Read, Update, Delete)
# list (변경가능) - CRUD 모두 가능
[1, 2, 3]

# tuple (변경불가능) -Read만 가능
(1, 2, 3)

# set - 중복이 불가능하고 순서가 없다. (= 리스트나 튜플은 중복가능, 순서있음)
# 정렬이 된 것처럼 보여도 우연일 뿐이다!
{1, 2, 3}

set1 = {1, 2, 3, 4}
print(set1)
set1.add(5)
print(set1)

리스트 = [1, 3, 4, 6, 1, 4, 2]
# 리스트에서 중복을 없애고 싶다? set으로 변환
set2 = set(리스트)
print(리스트)
리스트 = list(set2)  # 타입을 바꿔서 원하는 작업을 한 후 목적을 달성했으면 다시 원래 타입으로 바꿔줘야함.


# dictionary (이름(key)과 값(value)을 가짐)
{
    "name": "홍길동",
    "age": 20
}
