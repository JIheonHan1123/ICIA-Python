# 방명록 CRUD 연습
import model as m
import flask as f
app = f.Flask(__name__)


# 방명록 목록 출력
@app.route('/')
def list():
    gb = m.findall()
    return f.render_template('list.html', gb=gb)


# 방명록 저장 (추가하면 추가한 방명록이 목록에 뜨게)
@app.route('/write', methods=['post'])
def write():
    gname = f.request.form.get('gname', type=str)
    content = f.request.form.get('content', type=str)
    m.save(gname=gname, content=content)
    return f.redirect('/')


# 방명록 삭제
@ app.route('/delete', methods=['post'])
def delete():
    del_gno = f.request.form.get('gno', type=int)
    m.delete(del_gno=del_gno)
    return f.redirect('/')


# 변경
@app.route('/update', methods=['post'])
def update():
    gno = f.request.form.get('gno', type=int)
    content = f.request.form.get('content', type=str)
    m.update(gno=gno, content=content)
    return f.redirect('/')


app.run(debug=True)
