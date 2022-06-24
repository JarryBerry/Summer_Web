from flask import Flask, session
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

username = "stranger"

@app.route("/")
@app.route("/home")
def get_index():
    global username
    if username == None:
        return redirect(url_for('get_login'))
    return render_template('home.html', name=username)

@app.route("/other")
def get_other():
    global username
    if username == None:
        return redirect(url_for('get_login'))
    return render_template('other.html', name=username)

@app.route("/login", methods=['GET'])
def get_login():
    global username
    if username != "stranger":
        return redirect(url_for('get_index'))
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def post_login():
    global username
    username = request.form.get("username", None)
    return redirect(url_for('get_index'))

@app.route("/logout", methods=['GET'])
def get_logout():
    global username
    username = None
    return redirect(url_for('get_login'))

@app.route("/register", methods=['GET'])
def get_register():
    if 'username' in session:
        return redirect(url_for('get_index'))
    return render_template('register.html')

@app.route("/register", methods=['POST'])
def post_register():
    username = request.form.get("username", None)
    if username == None:
        return redirect(url_for('get_register'))
    password = request.form.get("password", None)
    if password == None:
        return redirect(url_for('get_register'))
    repeated = request.form.get("repeated", None)
    if repeated == None:
        return redirect(url_for('get_register'))
    if repeated != password:
        print("Repeated password does not match password!")
        return redirect(url_for('get_register'))
    # TODO: Do we have a user with this name already?

    # TODO: Store the user credentials

    # return the logged-in user to a session
    session['username'] = username
    return redirect(url_for('get_index'))
