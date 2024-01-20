def sample1():
    return 10


def sample2():
    print('hello')
# return이 없는 함수는 테스트가 안된다


def is_adult(age: int) -> bool:
    return age >= 18
# ex1) 나이를 입력받아 성년/미성년을 판단하는 함수


def get_fees(age: int):
    if age >= 25 and age <= 64:
        return 3000
    return 0
# ex2) 나이를 입력받아 입장료를 리턴하는 함수
# 25~64세면 3000원, 기타는 무료


def get_fees2(peoplenum: int):
    if peoplenum >= 10:
        return 2400*peoplenum
    return 3000*peoplenum
# ex3) 입장료는 3천원. 10명이상 1인당 2400원
# 인원수를 입력받아 요금 출력
