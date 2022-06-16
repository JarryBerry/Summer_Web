from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def get_index():
    return "<p>This is in my index function!!!!!!!!!!!!!</p>"

@app.route("/hello")
def get_hello():
    return render_template('hello.html', name="Jarrett")


@app.route("/not_jarrett")
def get_notHello():
    return render_template('hello.html', name="Santa")