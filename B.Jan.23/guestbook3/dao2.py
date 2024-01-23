# 연습

board_list = []
bno = 1

# save


def save(title: str, content: str, writer: str) -> bool:
    global bno
    b = dict(bno=bno, title=title, content=content, writer=writer, readcnt=0)
    board_list.append(b)
    bno += 1
    return True
