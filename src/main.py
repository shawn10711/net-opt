import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html' ,route_name='index')

@app.route('/insights')
def insights_view():
    return render_template('insights.html' )

@app.route('/performance')
def performance_view():
    return render_template('performance.html')

@app.route('/management')
def management_view():
    return render_template('management.html')

@app.route('/security')
def security_view():
    return render_template('security.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
