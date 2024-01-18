from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

# ex1) 태어난 년도를 입력받아 나이를 출력
# 화면2개 만들어야함 (년도를 입력하는 화면, 결과를 출력하는 화면 )


# 년도를 입력하는 화면
@app.route("/age_view")
def age_view():
    return render_template("age_view.html")


# 결과를 출력하는 화면
@app.route("/age_result")
def age_result():
    this_year = datetime.datetime.now().year
    birth_year = int(request.args['birth_year'])
    age = this_year - birth_year
    return render_template("age_result.html", age=age)


app.run()
