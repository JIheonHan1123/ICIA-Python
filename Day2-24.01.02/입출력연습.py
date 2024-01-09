# 숫자 2개를 입력 받아 다음과 같이 출력하시오
# 3과 8의 합은 11, 곱은 24입니다.
"""
num1 = int(input('num1 입력>> '))
num2 = int(input('num2 입력>> '))
sum = num1 + num2
mul = num1 * num2
print(f'{num1}과 {num2}의 합은 {num1+num2}, 곱은 {num1*num2}입니다')
print(f'{num1}과 {num2}의 합은 {sum}, 곱은 {mul}입니다')
"""

# 5와 8중 큰 수는 8, 작은 수는 5입니다.
'''
num1 = int(input('num1 입력>> '))
num2 = int(input('num2 입력>> '))
max = max(num1, num2)
min = min(num1, num2)
print(f'{num1}와 {num2}중 큰 수는 {max}, 작은 수는 {min}입니다')
'''

# 초를 입력 받아 몇분 몇초인지 출력
# ex) 210초라고 입력하면 3분 30초 출력
'''
input_second = int(input('초 입력>> '))
minute = input_second//60
new_second = input_second % 60
print(f'{minute}분 {new_second}초')
'''

# 분, 초를 입력하면 초를 출력
# ex) 5분 10초 >> 310초
'''
input_minute = int(input('분 입력>> '))
input_second = int(input('초 입력>> '))
new_sec1 = input_minute*60
print(f'{new_sec1+input_second}초')
'''

# 몇 일인지 입력받아서 몇개월 며칠인지 출력
# 333일 -> 11개월 3일
'''
input = int(input('입력>> '))
month = input//30
day = input%30
print(f'{month}개월 {day}일')
'''

# 분, 초 입력하는 예제 literal 줄이기
'''
input_minute = int(input('분 입력>> '))
input_second = int(input('초 입력>> '))
# 상수는 대문자로
SECONDS_PER_MINUTE = 60
result = input_minute*SECONDS_PER_MINUTE + input_second
print(f'{result}초')
'''

# 몇개월 며칠인지 출력하는 예제 literal 줄이기
'''
input = int(input('입력>> '))
DAYS_PER_MONTH = 30
month = input//DAYS_PER_MONTH
day = input % DAYS_PER_MONTH
print(f'{month}개월 {day}일')
'''

# 섭씨를 입력 받아 화씨로 출력하시오
# (25°C × 9/5) + 32 = 77°F
'''
celsius = int(input('섭씨온도 입력>> '))
fahrenheit = celsius*1.8 +32
print(f'화씨온도는 {fahrenheit}°F')
'''

# 온도와 온도의 종류를 입력받아서
# 섭씨면 화씨로, 화씨면 섭씨로 변환
'''
temp = int(input('온도 입력>> '))
temp_Type = input('온도 종류 입력>> ')

if temp_Type == '섭씨':
    print(f'{temp*1.8 + 32}°F')
else:
    print(f'{(temp-32)/1.8}°C')
'''

