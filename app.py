from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO
import utils

app = Flask(__name__)
app.secret_key = utils.secretkey


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # if user not in session:
    #     return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET": # What people see when they click "Login"
        if "user" in session:
            print session['user']
            return redirect("/home")
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form['username'] or ""
        password = form['password'] or ""
        if utils.login(username, password):
            session['user'] = username
        else:
            return "<err>Incorrect Username or Password</err>"


if __name__ == "__main__":
    app.debug = True
    #app.secret_key = utils.secret_key
    app.run(port=8000)
