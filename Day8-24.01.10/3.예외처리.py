# 예외(Exception): 실행 중 발생하는 오류
# 예외처리: 예외가 발생했을 때 오류 메시지를 내고 정상 종료하게 하자
# try~ except~
# try: 예외가 발생할 수 있는 코드
# except: 예외가 발생하면 실행할 코드

# int 받아오는 코드에 다른 타입이 들어왔을 때 예외처리
'''
try:
    score = int(input('점수입력>> '))
    # 아래 코드는 try문 안으로 들어와야 함
    # try안에있는 코드는 실행이 된다는 보장이 없음 => score가 있을 수도 있고 없을 수도 있다
    # 그래서 위 코드에서 문제가 발생하면 바로 except로 빠진다.
    if score >= 70:
        print('합격')
    else:
        print('불합격')
except:
    print('점수를 숫자로 입력하세요')
'''

# ex1) 정수변수 2개를 만들어, 나눗셈 결과를 출력하시오
# 예외처리가 필요하면 예외처리 하시오 -> 예외: 0으로 나눌 경우
a = 10
b = 0


def nanutsam(a: int, b: int):
    return a/b


try:
    print(nanutsam(a, b))
except:
    print('0으로 나눌 수 없습니다.')
