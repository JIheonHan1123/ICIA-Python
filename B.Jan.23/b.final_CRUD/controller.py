import flask as f
import dao
app = f.Flask(__name__)


@app.route('/')
def list():
    result = dao.findall()
    return f.render_template('list.html', list=result)


@app.route('/read')
def read():
    return f.render_template('read.html')


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


app.run(debug=True)
