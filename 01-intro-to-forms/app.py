from flask import Flask, session
from flask import render_template
from flask import request, redirect, url_for
import json
import werkzeug
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key="ksmdflkji240[i2hjfsklnf"

username = "stranger"

@app.route("/")
@app.route("/home")
def get_index():
    if 'username' in session:
        username = session['username']
    else:
        return redirect(url_for('get_login'))
    return render_template('home.html', name=username)

@app.route("/other")
def get_other():
    if 'username' in session:
        username = session['username']
    else:
        return redirect(url_for('get_login'))
    return render_template('other.html', name=username)

@app.route("/login", methods=['GET'])
def get_login():
    if username in session:
        return redirect(url_for('get_index'))
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get("username", None)
    if username != None:
        session['username'] = username
        return redirect(url_for('get_index'))
    else:
        return redirect(url_for('get_login'))

    try:
        with(f"storage/{username}.json","r") as f:
            creds = json.load(f)
    except Exception as e:
        print(f"Error in reading credentials! {e}")
        return redirect(url_for('get_login'))
    password = request.form.get("password", None)
    if not check_password_hash(creds['password'], password):
        print(f"Error - Bad password!")
        return redirect(url_for('get_login'))

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
    for c in username.lower():
        if not((c.isalpha() or c.isdigitc) or (c in '.-_')):
            print("Illegal characters in username!")
            return redirect(url_for('get_register'))
    password = request.form.get("password", None)
    if password == None:
        return redirect(url_for('get_register'))
    if len(password) < 8:
        print("Password is not long enough!")
        return redirect(url_for('get_register'))
    repeated = request.form.get("repeated", None)
    if repeated == None:
        return redirect(url_for('get_register'))
    if repeated != password:
        print("Repeated password does not match password!")
        return redirect(url_for('get_register'))
    # TODO: Do we have a user with this name already?
    try:
        with(f"storage/{username}.json","r") as f:
            creds = json.load(f)
            print("User already exists!")
            return redirect(url_for('get_index'))
    except Exception as e:
        print(f"Error in reading credentials! {e}")
        return redirect(url_for('get_login'))

    # TODO: Store the user credentials
    creds = {
        "username":username,
        "password":generate_password_hash(password)
    }
    with open(f"storage/{username}.json","w") as f:
        json.dump(creds, f)

    # return the logged-in user to a session
    session['username'] = username
    return redirect(url_for('get_index'))
