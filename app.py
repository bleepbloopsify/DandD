from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO
import utils

app = Flask(__name__)
app.secretkey = utils.secretkey


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # if user not in session:
    #     return redirect("/login")
    return render_template("index.html")

@app.route("/login")
def login():
    if user in session:
        return redirect("/home")
    session['user'] = "here"
    return render_template("login.html")


if __name__ == "__main__":
    app.debug = True
    #app.secret_key = utils.secret_key
    app.run(port=8000)
