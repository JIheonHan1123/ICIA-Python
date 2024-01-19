# ex1) 이름과 나이를 입력받아 다음과 같은 출력
# 홍길동님은 성년입니다 or 홍길동님은 미성년입니다
# 단, 성년일 경우 글자색 파랑, 미성년인 경우 글자색은 빨강

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/work", methods=['get'])
def work_input():
    return render_template('work_input.html')


@app.route("/work", methods=['post'])
def work_print():
    # inputname = request.form['inputname'] 이렇게 딕셔너리로 꺼낼 수 있는데
    # 메소드 형식으로 꺼내와서 타입을 지정해줄 수 있다
    # inputname = request.form.get('inputname', type=str, default='홍길동')
    # 여기서 default는 값이 아무것도 없을 때 기본으로 들어갈 값을 설정해주는거
    inputname = request.form.get('inputname', type=str)
    inputage = request.form.get('inputage', type=int)

    # 성년/미성년 계산
    # if나 for는 flask에서 할 수도 있고 html에서도 가능하다
    # flask에서 계산
    is_adult = inputage >= 18

    # html에서 계산
    # html에서 바로 하는게 좀 더 간단함(파이썬 코드가 간단해서 그럼)
    # 저렇게 계산 안하고 바로 html파일 {% %}부분에 if age>18 이런식으로 걸어주면 됨
    # 근데 웬만하면 front가 복잡한거보다 back이 복잡한게 더 나아서 파이썬에서 작업하자

    return render_template('work_print.html', name=inputname, age=inputage, is_adult=is_adult)


app.run(debug=True)
