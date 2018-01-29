from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo

app = Flask(__name__, static_folder='static')
mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('landing-page.html')

@app.route('/first')
def challenge1():
    return render_template('first_challenge.html')

@app.route('/second')
def challenge2():
    return render_template('second_challenge.html')

@app.route('/third')
def challenge3():
    return render_template('third_challenge.html')

@app.route('/fourth')
def challenge4():
    return render_template('fourth_challenge.html')

@app.route('/fifth')
def challenge5():
    return render_template('fifth_challenge.html')

@app.route('/temp')
def temp():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(threaded = True)