from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/m', methods=['get'])
def month_select():
    return render_template('select.html')


@app.route('/m', methods=['post'])
def month_result():
    # 난 html에서 계산함
    # month = request.form.get('month', type=int)
    # return render_template('result.html', month=month)

    # 강사님은 파이썬으로 계산
    # month = request.form.get('month', type=int)
    # season = '겨울'
    # if 3 <= month <= 5:
    #     season = '봄'
    # elif 6 <= month <= 8:
    #     season = '여름'
    # return render_template('result2.html', month=month, season=season)
    # 근데 이렇게 하면 글자별 색상 변경하는 것 때문에 html에서 또 {% if문 %}을 써야한다
    # 스타일을 줄 class 이름도 주면 된다.
    month = request.form.get('month', type=int)
    style = 'winter'
    season = '겨울'
    if 3 <= month <= 5:
        season = '봄'
        style = 'spring'
    elif 6 <= month <= 8:
        season = '여름'
        style = 'summer'
    elif 6 <= month <= 8:
        season = '가을'
        style = 'fall'
    return render_template('result2.html', month=month, season=season, style=style)


app.run(debug=True)
