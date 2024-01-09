# day1, day2복습

# 신씨가 소리질렀다. "도둑이야". 출력
'''print('신씨가 소리질렀다. "도둑이야".')'''

# 출력
# naver;kakao;sk;samsung
# naver/kakao/sk/samsung
'''
print('naver;kakao;sk;samsung')
print('naver/kakao/sk/samsung')
print('naver', 'kakao', 'sk', 'samsung', sep=';')
print('naver', 'kakao', 'sk', 'samsung', sep='/')
'''

# 삼전주식을 5만원에 10주 구입했다.
# 현재 나의 손익금액을 출력하시오 cf) 현재 77000원
'''
my_ex_samsung_electronics = 50000
current_samsung_electronics = 77000
stock_10 = 10
investment_amount = my_ex_samsung_electronics*stock_10  # 투자금액
gain_or_loss = current_samsung_electronics*stock_10 - investment_amount  # 평가손익
print(gain_or_loss)
'''

# 아래 모양이 나오도록 출력
# @@@@@@@@@@
# @        @
# @        @
# @        @
# @@@@@@@@@@
'''
print('@'*10)
print('@        @')  # print('@', ' '*6, '@')
print('@        @')  # print('@', ' '*8, sep='')
print('@        @')  # print('@', '@', sep='        ')
print('@'*10)
'''

# 입력을 받아올 때
'''
username = input('아이디 입력>> ')
age = input('나이 입력>> ')
print(type(username))
print(type(age))
age = int(age)
print(type(age))
'''

# 국어, 영어 점수를 입력받아 합계와 평균을 입력
'''
kor = int(input('국어점수 입력>> '))
eng = int(input('영어점수 입력>> '))
sum = kor + eng
avg = sum/2
print(f'합계:{sum}점, 평균:{avg}점')
'''

# 집의 가로와 세로를 입력받아 너비를 평으로 출력하시오
# cf) 3.3제곱미터가 1평
'''
width = int(input('가로>> '))
length = int(input('세로>> '))
area = width*length
PYEONG = 3.3
result = area/PYEONG
print(result)
'''

# 월급입력 >> 연봉출력
# 월급입력 >> 소득세, 소득세를 제외한 실수령액 출력
# cf) 소득세율은 연봉의 3.3%
'''
salary_for_month = int(input('월급입력>> '))
ONE_YEAR = 12
salary_for_year = salary_for_month*ONE_YEAR
print(salary_for_year)

INCOME_TAX_RATE = 0.033
income_tax = salary_for_year * INCOME_TAX_RATE
actual_receipt = salary_for_year - income_tax
print(f'소득세: {income_tax}, 실수령액: {actual_receipt}')
'''

# 반지름을 입력받아 원의 면적(파이*반지름^2)과 원의 둘레(2*파이*반지름) 출력
'''
r = int(input('반지름 입력>> '))
PI = 3.14
area = PI*r*r
circumference = 2*PI*r
print(f'원의 면적은 {area}, 원의 둘레는 {circumference}')
'''


# day3

# 숫자를 입력받아 3의 배수인지 아닌지 출력
'''
input_number = int(input('숫자입력>> '))
if input_number % 3 == 0:
    print('3의 배수 O')
else:
    print('3의 배수 X')
'''

# 점수를 입력받아 90이상 우수, 70이상 패스, 미만이면 낙제
'''
input_score = int(input('점수입력>> '))
if input_score >= 90:
    print('우수')
elif input_score >= 70:
    print('패스')
else:
    print('낙제')
'''

# 국어 영어 모두 70이상이면 합격, 아니면 불합격
'''
kor, eng = 75, 65
if kor>=70 and eng>=70:
    print('합격')
else:
    print('불합격')
'''

# 숫자를 입력받아 양수면 그대로, 음수면 양수로 바꿔서 출력
'''
input_num = int(input('숫자입력>> '))
if input_num > 0:
    print(input_num)
else:
    print(-input_num)
'''

# 길이를 입력받아 센티미터>인치, 인치>센티미터 변환
# cf) 1인치 = 2.54cm
'''
length = int(input('길이입력>> '))
length_type = input('cm 또는 inch 입력>> ')
INCH = 2.54
if length_type == 'cm':
    print(f'{length/INCH} inch')
elif length_type == 'inch':
    print(f'{length*INCH} cm')
else:
    print('cm 또는 inch를 입력하세요')
'''

# 임의로 가정
# 남자의 적정체중은 (키-100)
# 여자의 적정체중은 (키-105)
# 키를 입력 받아 적정체중 출력
'''
height = int(input('키 입력>> '))
gender = input('성별입력(남자면 m/ 여자면 f)>> ')

if gender == 'm':
    print(f'당신의 적정 체중은 {height-100}kg 입니다.')
elif gender == 'f':
    print(f'당신의 적정 체중은 {height-105}kg 입니다.')
else:
    print('m 또는 f를 선택해주세요')
'''
