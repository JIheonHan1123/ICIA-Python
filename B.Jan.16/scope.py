# scope: 변수의 사용범위, 파이썬에서 스코프는 함수에 의해서 생김 =함수 스코프
x = 10


def func1():
    x = 30
    print('함수 안에서:', x)


print('함수 밖에서:', x)
func1()
