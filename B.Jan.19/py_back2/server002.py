from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/namecity', methods=['get'])
def namecity():
    return render_template('nc_input.html')


@app.route('/namecity', methods=['post'])
def namecity_print():
    inputname = request.form['inputname']
    inputcity = request.form['inputcity']
    return render_template('nc_output.html', name=inputname, city=inputcity)


app.run(debug=True)
