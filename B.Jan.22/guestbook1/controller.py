import flask as f
import model as m

# 플라스크 앱(백엔드 서버)을 생성
app = f.Flask(__name__)


# 컨트롤러는 주소를 지정해주고 모델과 뷰를 연결해주는 역할을 한다
# 방명록 출력: /만 주면 주소가 127.0.0.1:5000라서 메인페이지에 자주 씀
@app.route('/')
def list():
    guestbook = m.findall()
    # list.html에 guestbook을 넘길건데 gb란 이름으로 넘겨준다
    return f.render_template("list.html", gb=guestbook)


@app.route('/write', methods=['post'])
def write():
    content = f.request.form.get('content', type=str)
    # 모델에 save를 넘겨줌
    m.save(content=content)

    # render_template은 화면출력하는거(get)
    # redirect는 주소이동시키는거(post. 처리가 끝났으면 이동)
    return f.redirect("/")


@app.route("/delete")
def delete():
    gno = f.request.args.get('gno', type=int)
    m.delete(gno)
    return f.redirect("/")


# 서버를 개발자모드로 실행(개발자모드: 변경하면 자동 재실행)
app.run(debug=True)
