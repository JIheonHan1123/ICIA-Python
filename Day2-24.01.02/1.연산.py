# day2, day3


# day2

# 연산
# 산술연산
# +(더하기), -(빼기), *(곱하기), /(나누기), //(몫), %(나머지)

print(18/5)
print(18//5)
print(18 % 5)
print(17 % 5)

# 소수점 이하를 버리고 출력 (연산만 사용해서)
x = 15.82
print(x//1)  # 15.0이 나온다.

# %연산 금지. a/b의 나머지를 출력하시오
a, b = 19, 5
c = a//b
print(a-b*c)
# 나머지 = 나눌 수 - (나누는 수 * 몫)
# 나머지 = a - (b * (a//b))

# y를 1의 자리에서 버림
y = 453  # 450 나와야함
result = y - y % 10
print(result)

# y를 1의 자리에서 버림 (%금지)
r = y - (y-(10*(y//10)))
print(r)

# 집에서 해보던가
# 1. 숫자를 입력하면 그 숫자보다 작은 최대의 짝수 ex) 7 >> 6
'''
num = int(input('숫자입력>> '))
result = num//2 * 2
print(result)
'''

# 2. 숫자를 입력하면 그 숫자 이상의 가장 큰 7의 배수 ex) 17 >> 21 cf) 21넣으면 21나와야 함
'''
# number = int(input('숫자입력>> '))
# result = (number//7+1) * 7
# print(result)
'''
number = int(input('숫자입력>> '))
result = ((number + 6) // 7) * 7
print(result)


# day3
# 숫자연산: + - * /, //, %
# 비교연산: > >= < <= == != :연산결과가 bool
# 논리연산: not, and, or :연산대상이 bool (결과도 bool)
# 대입연산: a=0 \ a=a+1
a = 10
a = a+1  # a+=1
a = a*5  # a*=5

# 숫자연산
# 문자에 대해서는 +, * 성립
print('hello ' + 'java')
print('hello ' * 5)

# 비교연산 (비교연산은 총 6가지)
# <, <=, >, >=, ==, !=
print(5 > 3)
print(type(5 > 3))  # 비교연산의 결과는 bool

print(5 < 3)
print(type(5 < 3))

print(5 >= 3)
print(type(5 >= 3))

print(5 <= 3)
print(type(5 <= 3))

print(5 == 3)
print(type(5 == 3))

print(5 != 3)
print(type(5 != 3))

# 논리연산 (not, and, or)

# not (논리부정)
kor, eng = 75, 80
print(not kor > 70)  # True지만 앞에 not이 붙어서 False가 나온다

# and (모두 참이어야 참, 하나라도 거짓이면 거짓)
num = 70
# num이 0이상인지 출력
print(num >= 0)
# num이 100이하인지 출력
print(num <= 100)
# num이 0에서 100사이인지 출력
print(num >= 0 and num <= 100)
print(0 <= num <= 100)

# or (하나라도 참이면 참)
num = 70
# num이 0보다 작거나 100보다 큰가?
print(num < 0 or num > 100)
print(not (num >= 0 and num <= 100))
