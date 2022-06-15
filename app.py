from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_index():
    return "<p>This is in my index function!!!!!!!!!!!!!</p>"

@app.route("/hello")
def get_hello():
    return "<p>Hello and Welcome to Flask!!!!</p>"