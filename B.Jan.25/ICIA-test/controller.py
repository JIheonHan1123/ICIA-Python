import flask as f
import dao

app = f.Flask(__name__)


@app.route('/')
def list():
    board_list = dao.list()
    return f.render_template('list.html', list=board_list)


@app.route('/write')
def write_view():
    return f.render_template('write.html')


@app.route('/write', methods=['post'])
def write():
    title = f.request.form.get('title', type=str)
    content = f.request.form.get('content', type=str)
    nickname = f.request.form.get('nickname', type=str)
    dao.save(title=title, content=content, nickname=nickname)
    return f.redirect('/')


@app.route('/read')
def read():
    bno = f.request.args.get('bno', type=int)
    readcnt = f.request.args.get('readcnt', type=int)
    board = dao.read(bno)
    return f.render_template('read.html', board=board, readcnt=readcnt)


@app.route('/update', methods=['post'])
def update():
    bno = f.request.form.get('bno', type=int)
    title = f.request.form.get('title', type=str)
    content = f.request.form.get('content', type=str)
    dao.update(bno=bno, title=title, content=content)
    return f.redirect('/')


@app.route('/delete', methods=['post'])
def delete():
    bno = f.request.form.get('bno', type=int)
    dao.delete(bno=bno)
    return f.redirect('/')


app.run(debug=True)
