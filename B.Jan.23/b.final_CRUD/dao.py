
board_list = []

board_list.append(dict(bno=1, title='aa', content='aaa', nickname='hhs', readcnt=0))
board_list.append(dict(bno=2, title='bb', content='bbb', nickname='hhs', readcnt=0))
board_list.append(dict(bno=3, title='cc', content='ccc', nickname='hhs', readcnt=0))
bno = 4


def save(title: str, content: str, nickname: str) -> bool:
    global bno
    b = dict(bno=bno, title=title, content=content, nickname=nickname, readcnt=0)
    board_list.append(b)
    bno += 1
    return True


def findall() -> list:
    return board_list


def findone(bno: int) -> dict:
    for board in board_list:
        if bno == board['bno']:
            board['readcnt'] += 1
            return board
    return None


def delete(bno: int) -> bool:
    for board in board_list:
        if bno == board['bno']:
            board_list.remove(board)
            return True
    return False
