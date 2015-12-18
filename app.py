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
    if request.method=="GET": # What people see when they click "Login"
        if "user" in session:
            return redirect("/home")
        return render_template("login.html")
        
    else: # Logging in, currently only accepts uname "DM" and pwd "DandD"
        u = request.form["username"]
        p = request.form["password"]
        if utils.auth(u,p):
            return render_template("login.html")
        return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    #app.secret_key = utils.secret_key
    app.run(port=8000)
