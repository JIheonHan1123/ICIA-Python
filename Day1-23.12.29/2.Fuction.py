# day1, day2, day3

# 함수: 언어들이 제공하는 기능(이름을 가진 기능), 이름을 가진 코드 덩어리
# 호출(call) -> () :함수이름치고 "괄호열고 닫는게" 호출, 호출을 해줘야만 실행이 된다.
# 나중에 재사용해야 생산성이 높아짐(값을 변수에 담아서 사용)

# 함수가 동작하려면 내가 원하는 값을 넘겨줘야 한다. -> 파라미터(인자)

# ex)
# print(3) -여기서 3은 파라미터(인자) or 심부름 값
# print()  -print함수는 인자를 주지 않으면 그냥 공백
# print(3.14)
# print(3+3)
# print('3'+'3')
# print(3,4,5,'')

# 인자 중에 이름이 정해진 인자가 있음
# sep
print(3, 4, 5)  # 이러면 3 4 5가 출력되는데 345를 출력하고 싶을 때
print(3, 4, 5, '')  # 이렇게 하면 그냥 값이 4개인 거임
print(3, 4, 5, sep='')  # 공백을 없애고 싶을 때 (공백 대신에 빈문자열)
print(3, 4, 5, sep=';')  # 3;4;5 (공백 대신에 ;)
# end
print(3, 4, 5, end='')  # print가 끝나고 난 다음에 뭘 할거냐 -> 줄바꿈 대신 빈문자열 -> 줄 안바뀜

# 함수의 종류: print, type, int, float, str, bool, max ...
# 함수는 1가지 일만 담당한다. input-입력만 받는 함수, print-출력만 하는 함수

# -----------------------------------------------------------------------------------------------
# 변수: 값에다가 이름을 붙인 것 >> 값을 담는 상자(이름을 가진다)
# 언어에 따라 만드는 법이 다르다. (파이썬은 자바처럼 타입을 주지 않고 만들 수 있다)
# Java: int a = 10
# Python: a = 10

# 함수, 변수 >> 이름을 가진다 why? 재사용하려고
a = 80
score = 85
# score가 더 좋은 이름. why? 알아보기 쉬워서

# 상수
pi = 3.14  # 소문자 >> 값을 바꿔도 된다
PI = 3.14  # 대문자 >> 값을 바꾸지 말자 -> 상수

# 파이썬에서 변수의 이름이 겹치면 덮어쓴다 -> 그래서 변수 이름을 웬만하면 안겹치게 매우 신경써서 지어야 함
# 변수의 이름은 쉬어야 한다
a = 10
a = 20
a = 30
# 여기서 =는 등호가 아니라 대입. (오른쪽 값을 왼쪽으로 대입)
# "같다"는 ==를 사용

this_year = 2024
this_city = "인천"
lat_seoul = 37.33  # 위도: latitude
long_seoul = 127.00  # 경도: longitude

lat_seoul += 1
print(lat_seoul)


x = 10
y = 5

print(x)
print(y)
print(x+y)

print(type(x))

x = x-1
print(x)


# 정의: 변수나 함수를 만드는 것. (선언하는 것)
# 값만 존재하는 상태에서는 출력할 수 없다.

# 명명규칙 ex)성적합계는 220점이다.
SumOfAllScores = 220  # C
sumOfAllScores = 220  # Java
sum_of_all_scores = 220  # Python

# 1. 이름은 알아보기 쉽게 소문자, _로 만든다
# 2. 키워드(예약어)는 사용할 수 없다
# cf) 예약어: 파이썬이 사용하는 단어 ex) True, False, if, else, import ...
my_name = '한지헌'
age = 22

print(my_name)
print('제 이름은', my_name)  # ,로 붙이면 공백발생

age += 1  # age = age + 1
print('나이는', age, '살')

my_dog_name = '초코'
print('우리집 강아지 이름은', my_dog_name, '에요')
print(my_dog_name, '는 산책을 아주 좋아해요')

print('우리집 강아지 이름은 ' + my_dog_name + '에요')
print(my_dog_name + '는 산책을 아주 좋아해요')

salary = 3000000
print('급여 :', salary)
print('급여 : ' + str(salary))

samsung_electronics = 78500
stock_10 = samsung_electronics*10
print('평가금액:', stock_10)

# 최대값
print(max(3, 4))
m = max(3, 4)  # 결과적으로 m=4 랑 똑같음
print(m)

# 최소값
print(min(10, 20))
n = min(10, 20)  # 결과적으로 n=10 이랑 똑같음
print(n)

# 합
# print(sum(10,20)) -이건 에러
print(sum([10, 20]))
# sum 함수에는 하나의 데이터 덩어리가 와야한다.
# 값이 따로따로 있으면 안 됨.

print(max(3, 7, 10))
print(max([3, 7, 10]))

a = max(3, 7)
b = 10
print(a+b)

# input -입력을 받는 함수
name = input('이름 입력: ')
print('이름은', name)
print('이름은 ' + name)
print('이름은 name')
print(f'이름은 {name}')
your_hobby = input('취미: ')
print(f'당신의 취미는 {your_hobby}')

# 이름, 나이 입력 받아서 출력
name = input('이름입력>> ')
age = input('나이입력>> ')
print(f'이름: {name}, 나이: {age}')

# 숫자 2개 입력 받아서 출력
# 키보드로 입력한 건 모두 다 str임.
num1 = int(input('첫번째 숫자 입력>> '))
num2 = int(input('두번째 숫자 입력>> '))
print(num1 + num2)

val1 = None
val2 = None
val1 = input('첫번째 숫자: ')
val2 = int(input('두번째 숫자: '))
sum = int(val1)+val2
# val1처럼 사용할때마다 바꾸는 것보다 val2처럼 미리 바꿔놓는 것이 좋음
print(sum)
