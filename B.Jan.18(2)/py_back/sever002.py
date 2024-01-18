'''  Flask 기본 틀
from flask import Flask, request, render_template
app = Flask(__name__)
app.run()
'''

from flask import Flask, request, render_template
# cf) render_template (템플릿을 그린다)

app = Flask(__name__)


# ex1) 사용자가 입력한 값을 html로 출력
@app.route('/sample1')
def sample1():
    val = request.args['val']

    # val을 넘기는데 result라는 이름으로 넘겨라
    return render_template("sample1.html", result=val)

    # 여기까지만 하면 아직 html없기 때문에 실행이 안 됨
    # html폴더 만들어주고 실행하면 되는데 만드는 방법이 다 정해져 있다!
    # 현재 서버파일과 같은 위치에 templates폴더 만들고 이 폴더 밑에 html파일 만든다
    # ex) html파일 만들고 F5로 실행하고 뒤에 주소에 /sample1?val=10


# ex2) 사용자가 입력한 값들의 합을 html로 출력
@app.route('/add')
def sample2():
    val1 = int(request.args['val1'])
    val2 = int(request.args['val2'])
    result = val1 + val2

    # cf) 여기서 "sample2_.html"이름에 오타나면 500에러가 난다.
    return render_template("sample2_.html", result=result)


# 주소창에 직접 값을 입력하지 않게 만들어야함 ex3) 덧셈을 입력할 화면을 출력
@app.route('/add_view')
def sample2_view():
    return render_template("sample2_view.html")
    # 여기까지는 입력할 화면 띄워주는 코드고
    # 값 입력하고 submit할 주소는 위에 만들었던 ~/add
    # 차피 같은 서버(파일)에 있는거라 그냥 /add만 줘도 됨


app.run()
