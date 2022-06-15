from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_index():
    return "<p>This is in my index function!</p>"

