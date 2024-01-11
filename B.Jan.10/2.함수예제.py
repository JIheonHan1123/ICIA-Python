# 1. 두 숫자를 입력받아 큰 수를 가리는 함수
def bigger_num(num1: int, num2: int):
    if num1 > num2:
        return num1
    else:  # 같은 수가 입력되어도 아무거나 리턴하도록
        return num2


# 2. 숫자를 입력받아 절대값을 계산하는 함수
def abs_check(num: int):
    if num < 0:
        return -num
    return num


''' 이거랑 위에랑 똑같은 거임. (if-else인 경우에 else를 써도되고 안써도 된다.)
def abs_check(num: int):
    if num < 0:
        return -num
    else:
        return num
'''

# 3.
