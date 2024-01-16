# 복습

# 원시타입 (primitive) - 8개 (언어마다 다름)
# 그냥 처음부터 사용할 수 있는 타입

# 값 1개를 저장하는 타입
# 숫자 >> 정수(int), 실수(float)
# 문자열 >> str
# 참거짓 >> bool
# 값 여러개를 저장하는 타입 = 집합 = sequence
# list          [1,2,3]     C,R,U,D
# tuple         (1,2,3)     R(읽기전용)
# set           {1,2,3}
# dictionary    { key:value, '홍길동':175, '전우치':165, '임꺽정':180 }
#               ['홍길동','전우치','임꺽정'] >> key만 모은거 >> list
#               [175,165,180] >> value만 모은거 >> list
#               dictionary는 list가 합쳐진 형태

# 순서대로 읽고 쓴다: list, tuple
# 계산으로 위치 파악: set
# 키와 값의 쌍(pair): dictionary

# 더 많은 타입을 사용하고 싶으면
# import로 불러와서 타입을 확장해서 사용할 수 있다.


######################################################
# 숫자타입 -> 타입마다 사용할 수 있는 연산, 함수가 다르다
# 산술연산: + - * - / // %

# string 타입
str1 = '10'
str2 = "3.14"
str3 = '홀짝홀짝홀짝홀짝'
# str 연산
print(str1 + str2)  # 연결
print(str1 * 10)    # 반복
# 인덱스 연산 (순서로 접근) -> 시퀀스와 동일
print(str3[0])  # 홀
print(str3[5])  # 짝
print(str3[-1])  # 짝
# 슬라이싱(slicing) 연산 -> 시퀀스와 동일
print(str3[0:3])  # '0번째'부터 '3번째 전'까지 잘라라 >> 홀짝홀짝이 아니라 홀짝홀
print(str3[1:])
print(str3[::2])  # 시작위치 : 끝위치 : 간격 >> 홀홀홀홀


###############################
# 함수: 이름을 가진 기능 -> 왜 이름을 붙였냐? 재사용하려고
# import없이 사용할 수 있는 함수 = 내장함수

# 내장함수 abs - 절대값 구하는 함수
num1 = 10
print(abs(100))
print(abs(-100))
print(abs(num1))

# 내장함수 len - 길이를 재는 함수
print(len('hello'))
# print(len(15)) 에러 => len은 집합의 길이를 재는 함수
# str은 집합은 아니지만 집합취급 >> 문자열은 문자들의 집합


#####################################################################
# 문자열은 변경 불가능(immutable) cf) 변경가능은 mutable
str6 = 'hello'
# str6[0] = 'z'
print(str6)

str6 = 'hello'
str6 = 'python'  # 근데 얘는 변경한거 아닌가? >> ㄴㄴ 아니다.
# 자바로 치면 참조변수 (지금까지 일주일동안 했던 모든 변수는 참조변수)


# list는 변경 가능
list6 = ['h', 'e', 'l', 'l', 'o']
list6[0] = 'z'
print(list6)


####################
# replace : 치환
str7 = "010-1111-2222"
# 함수 : 소속없는 함수 + 소속있는 메소드
print(len(str7))
# method: 특정 타입 소속 -> 타입은 함수도 가질 수 있다.
str7.replace('-', '.')
str7.replace("-", ".")  # 이 상태로는 값이 안바뀐다!! (출력은 안했지만 아직 동작안하는 코드임)
print(str7)  # 와 안바뀌누? => 기본적으로 문자열은 바꿀 수 없다

# 대입해야함
str7 = str7.replace("-", ".")
print(str7)


# 971011-2010015 >> 971011-2****** 로 변환
j1 = "971011-2010015"
j1 = j1.replace("010015", "******")
print(j1)

j1 = "971011-2010015"
print(j1.replace(j1[8:], '******'))


# strip >> 앞 뒤 공백을 제거하는 함수
str5 = "    aa aa    "  # "aa aa" 이렇게 바꿔준다
# 가운데 공백을 지우지 않는 이유는 내용(띄어쓰기)일수도 있기 때문에 지우지 않는다.
print(str5.strip())

################################################
# bool
age = 30
gender = '여자'
city = '인천'
age >= 50 and gender == '여자'

(age >= 20 and gender == '여자') or city == '인천'


# 타입 재정립
# collection 타입(집합): list, tuple, set, dictionary
# sequence 타입(1다음 2 다음 3 이런식으로 순서대로보는거): list, tuple

# list와 tuple의 차이
# list는 mutable(가변), tuple은 immutable(불변)
list1 = [1, 3, 5]
tuple1 = tuple(list1)
list1 = list(tuple1)
print(list1)

# 데이터가 있다. Create Read Update Delete
# C
list1.append(100)
print(list1)

# R
# for 변수 in 컬렉션:
for x in list1:
    print(x)

# U
list1[1] = 200
print(list1)


# 'E
del list1[2]
print(list1)

# C - 추가
# R - 하나씩
# U, D - 찾아서


#############
# dictionary : 키(값의 이름)와 값(value)의 쌍
ice = {'바밤바': 1000, '옥동자': 1200, '월드콘': 2000}
ice2 = {"바밤바": 1000, "옥동자": 1200, "월드콘": 2000}
print(ice)
print(ice2)

# Read
print(ice['바밤바'])  # 1000이 나옴
# ex) 월드콘의 가격
print(f'{ice['월드콘']}원')

# Create (추가)
ice['아맛나'] = 1100
ice['빵빠레'] = 1500
print(ice)

# Update
ice['빵빠레'] = 1800
print(ice)

# Delete
del ice['아맛나']
print(ice)
