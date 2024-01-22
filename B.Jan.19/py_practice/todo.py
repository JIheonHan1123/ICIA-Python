# redirect: 새로운 주소로 이동 (post방식) -post로 들어오면 그 데이터를 처리하고 새로운 주소로 이동 (내가 클릭하거나 링크치고 엔터 누르면 리다이렉트임)
# render_template: html을 출력 (get방식) -get으로 들어오면 화면을 보여준다.

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


# 전역 변수: 모든 함수가 접근가능한 공유 데이터
todos = []
tno = 1


# 내용을 출력하는지
@app.route("/list")
def list():
    return render_template('list.html', todos=todos)


@app.route("/write")
def write_input():
    return render_template('write.html')


@app.route("/write", methods=['post'])
def do_write():
    global tno
    title = request.form.get('title', type=str)
    todo = {'tno': tno, 'title': title, 'finish': False}
    todos.append(todo)
    tno = tno + 1
    return redirect("/list")


@app.route('/delete', methods=['post'])
def delete():
    # 이름 안 같아도 되네?
    # 뒤에오는 tno와 같아야 하는건 html의 name속성의 값
    del_tno = request.form.get('tno', type=int)

    for todo in todos:
        if del_tno == todo['tno']:
            todos.remove(todo)
            break

    return redirect("/list")


app.run(debug=True)
