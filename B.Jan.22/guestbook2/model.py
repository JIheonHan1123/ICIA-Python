# 모델설계
# 방명록 = {번호, 이름, 내용, 작성일}의 딕셔너리로 구성된 리스트
import datetime as d
guestbook = []  # guestbook = list()를 써도 된다.

# dummy data 넣어보기
gb1 = dict(gno=1, gname="ㅎㅈㅎ", content="첫번째 방명록", writeday="2024-01-22")
gb2 = dict(gno=2, gname="ㅎㅎㅅ", content="두번째 방명록", writeday="2024-01-22")

# 사용자로부터 이름, 내용은 입력받을거임 => 입력한 내용은 html에서 테이블로 출력
guestbook.append(gb1)
guestbook.append(gb2)
gno = 3


# 모델은 데이터뿐만 아니라 함수까지 포함한걸 의미함
# 목록 출력 기능
def findall():
    return guestbook


# 내용 저장기능
def save(gname: str, content: str):
    global gno
    writeday = d.datetime.now().date()
    gb = dict(gno=gno, gname=gname, content=content, writeday=writeday)
    guestbook.append(gb)
    gno += 1


# 삭제 기능
def delete(del_gno: int):
    for gb in guestbook:
        if del_gno == gb['gno']:
            guestbook.remove(gb)


# 변경
def update(gno: int, content: str):
    for gb in guestbook:
        if gno == gb['gno']:
            gb['content'] = content
