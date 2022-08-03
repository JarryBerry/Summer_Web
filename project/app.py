from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def get_index():
    return render_template('index.html')
