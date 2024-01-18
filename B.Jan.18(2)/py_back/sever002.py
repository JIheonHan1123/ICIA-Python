'''  Flask 기본 틀
from flask import Flask, request, render_template
app = Flask(__name__)
app.run()
'''

from flask import Flask, request, render_template

app = Flask(__name__)


# 사용자가 입력한 값을 html로 출력
@app.route('/sample1')
def sample1():
    val = request.args['val']

    # val을 넘기는데 result라는 이름으로 넘겨라
    return render_template("sample1.html", result=val)

    # 여기까지만 하면 아직 html없기 때문에 실행이 안 됨
    # html폴더 만들어주고 실행하면 되는데 만드는 방법이 다 정해져 있다!
    # 현재 서버파일과 같은 위치에 templates폴더 만들고 이 폴더 밑에 html파일 만든다
    # ex) html파일 만들고 F5로 실행하고 뒤에 주소에 /sample1?val=10


app.run()
