# 반복
list1 = [1, 3, 5]

# 10 in list1 = 결과가 참거짓 (10이 list1에 있니?)

# list1의 원소를 하나씩 꺼내서 item에 담는 반복문
for item in list1:
    print(item)


# while은 뒤에 종료조건이 온다.
'''
index = 0
while index < 3:  # 조건이 참일 동안 계속 실행 -> 무한반복 가능
    print(list1[index])
    index += 1

while True:
    a = int(input('값을 입력하세요(999면 종료)>> '))
    if a == 999:
        print('이용해주셔서 감사합니다')
        break
    print(f'입력한 값: {a}')
'''

# 예제
"""
    1. 값 추가 -> input('숫자입력: ')
    2. 리스트 출력
    3. 999 들어오면 종료 -> 감사합니다
"""
'''
리스트 = []
while True:
    print('1. 값 추가')
    print('2. 리스트 출력')
    print('999. 999 누르면 종료')
    select = input('번호 선택: ')
    if select == '1':
        num = int(input('숫자입력: '))
        리스트.append(num)
    elif select == '2':
        print(리스트)
    elif select == '999':
        print('감사합니다')
        break
    else:
        print('메뉴를 정확하게 입력하세요')
'''

# cf
# sum(리스트) => 리스트의 합 출력
# 보완 -> 3. 누르면 리스트의 합 출력
'''
리스트 = []
while True:
    print('1. 값 추가')
    print('2. 리스트 출력')
    print('3. 리스트의 합 출력')
    print('999. 999 누르면 종료')
    select = input('번호 선택: ')
    if select == '1':
        num = int(input('숫자입력: '))
        리스트.append(num)
    elif select == '2':
        print(리스트)
    elif select == '3':
        print(f'입력값의 합계:{sum(리스트)}')
        # 엄밀히 말하면 f문자열 안에 변수가 들어가는게 아니라 파이썬 코드가 들어갈 수 있다.
    elif select == '999':
        print('감사합니다')
        break
    else:
        print('메뉴를 정확하게 입력하세요')
'''

# 보완 -> 4. 누르면 리스트의 평균출력
리스트 = []
while True:
    print('1. 값 추가')
    print('2. 리스트 출력')
    print('3. 리스트의 합 출력')
    print('4. 리스트의 평균 출력')
    print('999. 999 누르면 종료')
    select = input('번호 선택: ')
    if select == '1':
        num = int(input('숫자입력: '))
        리스트.append(num)
    elif select == '2':
        print(리스트)
    elif select == '3':
        print(f'입력값의 합계:{sum(리스트)}')
        # 엄밀히 말하면 f문자열 안에 변수가 들어가는게 아니라 파이썬 코드가 들어갈 수 있다.
    elif select == '4':
        print(f'입력값의 평균:{sum(리스트)/len(리스트)}')
    elif select == '999':
        print('감사합니다')
        break
    else:
        print('메뉴를 정확하게 입력하세요')
