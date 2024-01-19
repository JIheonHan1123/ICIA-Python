from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/m', methods=['get'])
def month_select():
    return render_template('select.html')


@app.route('/m', methods=['post'])
def month_result():
    # 난 html에서 계산함
    month = request.form.get('month', type=int)
    return render_template('result.html', month=month)

    # 강사님은 파이썬으로 계산
    # month = request.form.get('month', type=int)
    # season = '겨울'
    # if 3 <= month <= 5:
    #     season = '봄'
    # elif 6 <= month <= 8:
    #     season = '여름'
    # return render_template('result2.html', month=month, season=season)


app.run(debug=True)
