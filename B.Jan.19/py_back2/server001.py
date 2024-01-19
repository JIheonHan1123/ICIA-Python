# 사용자의 요청에 응답하는 서버 개발: 백엔드 + 화면
# 프레임워크 -필요한 기능들을 부품화해서 조립하는 방식
# 파이썬의 웹 프레임워크: Flask, Django, FastAPI -3개라 그랬음

# 이때 서버랑 같은 위치의 파일에 폴더 2개를 만들어줘야함.
# templates - html
# static - css, js

# 여기 안에 들어간 html은 단독으로 실행되어서는 안됨 (라이브서버로 열지않는다)
# 단독실행해도 아무 의미없음
# Flask로 여는거임
# 독립된게 아니라 Flask에 조직된 html (입력, 출력을 담당한다)


'''  Flask 기본 틀
from flask import Flask, request, render_template
app = Flask(__name__)
app.run()
'''

from flask import Flask, request, render_template
app = Flask(__name__)


# 배포서술자 (deployment descriptor: 함수와 주소의 쌍- 여기서는 aaa와 /hello)
@app.route('/hello')
def aaa():
    # 플라스크 함수의 리턴은 반드시 문자열
    # return 'hello'
    # render_template() 함수자체도 설명보면 str로 리턴하게 되어있음
    return render_template('index.html')


# ex1) 이름을 입력받는 html 파일을 웹애플리케이션(웹앱)에 추가하시오
@app.route('/name', methods=['get'])
def name():
    return render_template('name.html')


# get으로 오면 위에꺼 post로 오면 이거 실행되는거라 주소이름 똑같아도 됨
# 근데 함수이름은 달라야함(파이썬 특)
# get방식은 화면을 출력, post방식을 처리하고 받아온 이름을 출력
# !!!!!!!!!method에 s붙는거 주의(s안붙이면 실행할 때 에러남)!!!!!!!!!!!
@app.route('/name', methods=['post'])
def name_print():
    # get방식 요청 데이터: request.args
    # post방식 요청 데이터: request.form
    inputname = request.form['inputname']
    return render_template('name_result.html', rrrname=inputname)


# 현재 서버의 모든 url 출력
print(app.url_map)
# aaa대한 경로가 /hello라고 뜨는 것을 확인할 수 있다.


# 실행되는 url: 127.0.0.1:5000
# 어제 했던거 정정
# F5가 아니라 수동으로 실행하면 서버안끄고 계속 실행가능 python B.Jan.19/py_back2/server001.py
# 배포할때는 debug 꺼야 함
app.run(debug=True)
