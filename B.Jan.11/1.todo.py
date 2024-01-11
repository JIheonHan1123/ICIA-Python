# 할일은 할일번호, 할일, 완료여부로 구성
# 값 여러개 list, tuple, set -> 반복문 사용 가능

todos = []
todo = {}  # dictionary { "key" : value, ... }

todos.append({'tno': 1, 'title': '자바 공부', 'finish': False})
todos.append({'tno': 2, 'title': '스프링 공부', 'finish': False})
todos.append({'tno': 3, 'title': '파이썬 공부', 'finish': False})
print(todos)
tno = 4

# 함수를 일단 만들어 놓고 실행해보고 싶으면 함수 내용에 pass를 쓴다
'''
def print_todos():
    pass
'''


def print_todos():
    for todo in todos:
        print(todo)


def add_todo():
    # 함수 안에서 함수 밖에 있는 변수를 사용하려면 사용한다고 적어줘야함.
    global tno
    title = input('할일입력>> ')
    todos.append({'tno': tno, 'title': title, 'finish': False})
    tno = tno + 1
    print_todos()


def toggle_finish():
    tog_tno = int(input('변경할 일 번호입력>> '))
    found = False
    for todo in todos:
        if tog_tno == todo['tno']:
            todo['finish'] = not todo['finish']
            found = True
            print_todos()
    if found == False:
        print('번호를 제대로 입력하세요')


def delete_todo():
    del_tno = int(input('삭제할일 번호입력>> '))
    found = False
    for todo in todos:
        if del_tno == todo['tno']:
            todos.remove(todo)
            print_todos()
    if found == False:
        print('번호를 제대로 입력하세요')


while True:
    print('=== 할일 관리 ===')
    print('1.할일목록, 2.할일추가, 3.할일변경, 4.할일삭제, 999.종료')
    select = input('메뉴선택>> ')
    if select == '1':
        print_todos()
    elif select == '2':
        add_todo()
    elif select == '3':
        toggle_finish()
    elif select == '4':
        delete_todo()
    elif select == '999':
        print('이용해주셔서 감사합니다')
        break
    else:
        print('잘못된 메뉴선택입니다. \n다시 선택해주세요.')
