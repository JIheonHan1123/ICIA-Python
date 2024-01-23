import flask as f
import dao
app = f.Flask(__name__)


# 방명록 출력
@app.route('/')
def list():
    result = dao.findall()
    return f.render_template('list.html', list=result)


@app.route('/write', methods=['post'])
def write():
    nickname = f.request.form.get('nickname', type=str)
    content = f.request.form.get('content', type=str)
    dao.save(nickname=nickname, content=content)
    return f.redirect('/')


@app.route('/delete', methods=['post'])
def delete():
    gno = f.request.form.get('gno', type=int)
    dao.delete(gno)
    return f.redirect('/')


app.run(debug=True)
