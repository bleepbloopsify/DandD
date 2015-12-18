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
        if 'user' in session and session['user']:
            print session['user']
            return redirect("/home")
        return render_template("login.html")
    else:
        form = request.form
        username = form['username'] or ""
        password = form['password'] or ""
        if utils.auth(username, password):
            session['user'] = username
            return 'success'
        return 'fail'

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET": # What people see when they click "Login"
        if 'user' in session and session['user']:
            print session['user']
            return redirect("/home")
        return render_template("register.html")
    else:
        form = request.form
        username = form['username'] or ""
        password = form['password'] or ""
        confmpwd = form['confmpwd'] or ""
        if utils.register(username, password, confmpwd):
            session['user'] = username
            return 'success'
        return 'fail'

@app.route("/logout")
def logout():
    session['user'] = None
    return redirect('/login')


@app.route("/create_char", methods=["GET", "POST"])
#The page for creating a new character / editing character info
def create_char():
    if request.method == "GET": # So people can only access it while logged in
        return redirect("/home")
    else:
        return render_template("create_char.html")
@app.route("/game", methods=["GET", "POST"])
#The page where you can view the details of a game
def game():
    if request.method == "GET": # So people can only access it while logged in
        return redirect("/home")
    else:
        return render_template("game.html")
    
@app.route("/create_item", methods=["GET", "POST"])
#The page for creating new items / editing item info
def create_item():
    if request.method == "GET": # So people can only access it while logged in
        return redirect("/home")
    else:
        return render_template("create_item.html")

if __name__ == "__main__":
    app.debug = True
    #app.secret_key = utils.secret_key
    app.run(port=8000)
