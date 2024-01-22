import datetime as d
# model = 데이터 (+ 보통 함수까지 포함한 의미이다)
# 모델설계 = 디자인

# 방명록

# 파이썬에서 타입은 모두 클래스
# 클래스 이름으로 객체를 생성할 수 있다.
# 클래스 이름을 함수를 사용하듯이 사용할 수 있다.
guestbook = list()

# dictionary 만드는 두가지 방법
gb1 = {"gno": 1, "content": "첫번째 방명록", "writeday": "2024-01-22"}
'''
# 이런 함수가 있을 때
def hap(val1: int, val2: int) -> int:
    return val1+val2


# 이렇게 사용하는게 기본인데
hap(10, 20)
# val1에 10, val2에 20이 들어가야만 한다면 (값이 잘못 들어가는 것을 방지해야한다면)
# 이름을 지정해서 값을 넘길 수 있다.
hap(val2=20, val1=10)
'''
gb2 = dict(gno=2, content="두번째 방명록", writeday="2024-01-22")


guestbook.append(gb1)
guestbook.append(gb2)


gno = 3


# 모델 = 데이터 +함수까지
# 리스트 전부 출력 -스프링은 모델 함수이름이 정해져있다. 그 이름을 땡겨서 사용
def findall():
    return guestbook


def save(content: str):
    global gno
    writeday = d.datetime.now().date()
    gb = dict(gno=gno, content=content, writeday=writeday)
    guestbook.append(gb)
    gno += 1


def delete(gno: int):
    for gb in guestbook:
        if gb['gno'] == gno:
            guestbook.remove(gb)
