# todo (할 일)
'''
todos = [
    {'tno': 1, 'title': '자바공부', 'finish': False},
    {'tno': 5, 'title': '파이썬공부', 'finish': False}
]
# print(todos)
'''

# 왜 번호가 1다음에 5인가? >> 2,3,4번의 할 일은 끝내서 지워버렸다. -> 이러면 납득 가능

'''
tno = 6
# Create
title = input('할일 입력>> ')
todo = {"tno": tno, "title": title, "finish": False}
todos.append(todo)
tno = tno + 1

# Read: for문으로 todos 출력
for input_todo in todos:
    print(input_todo)

# Update: tno로 찾아서 finish를 toggle
#         못 찾으면 아무것도 하지 않는다.
input_tno = int(input('할 일 번호입력>> '))
for todo in todos:
    if input_tno == todo['tno']:
        todo['finish'] = not todo['finish']
        break
print(todos)

# Delete: tno로 찾아서 삭제
# 삭제하는 방법1: del list[idx]
# 삭제하는 방법2: list.remove(dictionary)
del_tno = int(input('삭제할 일 번호입력>> '))
for todo in todos:
    if del_tno == todo['tno']:
        todos.remove(todo)
        break
print(todos)
'''

# 연습 (할일관리할 리스트와 할일 번호가 필요함)
todos = [
    {'tno': 1, 'titile': '할일1', 'reg_day': '2024-01-09', 'finish': False},
    {'tno': 2, 'titile': '할일2', 'reg_day': '2024-01-09', 'finish': False},
    {'tno': 3, 'titile': '할일3', 'reg_day': '2024-01-09', 'finish': False},

]
tno = 2
# CRUD

# Read: 전체읽기, 1개읽기
for todo in todos:
    print(todo)

# 할일번호를 입력받아 할일을 찾아서 출력
todo_num = int(input('할일번호 입력>> '))
찾았니 = False
for todo in todos:
    if todo_num == todo['tno']:
        print(todo)
        break

if 찾았니 == False:
    print('할일이 없습니다.')
