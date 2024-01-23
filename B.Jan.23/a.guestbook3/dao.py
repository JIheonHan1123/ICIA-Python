# DAO =Data Access Object (model의 조작을 담당하는 파일)


# 여기는 model (데이터 자체)
import datetime as d
guestbook = []
gb = dict(gno=1, nickname='관리자', content='욕설, 비방은 경고없이 삭제합니다', writeday='2024-01-23')
guestbook.append(gb)

# 이런 일련번호는 보통 key로 사용된다.
# 문자열은 오타 위험이 있어서 통상 key는 숫자로 사용
gno = 2


# 여기부터는 dao (모델을 조작)
# Create
# 코드는 항상 테스트해야하는데 귀찮아서 안함. 최소한 리턴걸어주자(ex) ->bool 이런식으로)
def save(nickname: str, content: str) -> bool:
    global gno
    writeday = d.datetime.now().date()
    gb = dict(gno=gno, nickname=nickname, content=content, writeday=writeday)
    guestbook.append(gb)
    gno += 1
    return True


# Read
def findall() -> list:
    return guestbook


# Delete
# return: 함수를 종료하고 결과 값을 남겨라
# 함수에서는 return을 break 대신 사용할 수 있다
def delete(gno: int) -> bool:
    for gb in guestbook:
        if gno == gb['gno']:
            guestbook.remove(gb)
            return True
    return False
