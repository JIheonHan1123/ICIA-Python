import datetime as d

board_list = list()
bno = 1


# C
def save(title: str, content: str, nickname: str) -> bool:
    global bno
    writeday = d.datetime.now().date()
    board = dict(bno=bno, title=title, content=content, nickname=nickname, writeday=writeday, readcnt=0)
    board_list.append(board)
    bno += 1
    return True


# R -> findall
def list() -> list:
    return board_list


# R -> findone
def read(bno: int) -> dict:
    for board in board_list:
        if board['bno'] == bno:
            board['readcnt'] += 1
            return board
    return None


# U
def update(bno: int, title: str, content: str) -> bool:
    for board in board_list:
        if board['bno'] == bno:
            board['title'] = title
            board['content'] = content
            return True
    return False


# D
def delete(bno: int) -> bool:
    for board in board_list:
        if board['bno'] == bno:
            board_list.remove(board)
            return True
    return False
