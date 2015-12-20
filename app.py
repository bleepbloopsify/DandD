from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO
import utils

app = Flask(__name__)
app.secret_key = utils.secretkey

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")



@app.route("/create_char", methods=["GET", "POST"]) #The page for creating a new character / editing character info
def create_char():
    if request.method == "GET": # So people can only access it while logged in
        if 'user' in session and session['user']:
            return render_template("create_char.html")
        else:
            return redirect("/login/redirect")

@app.route('/games')# Page for viewing the list of all of your games
def games():
    return redirect("games.html")

@app.route("/gameinfo", methods=["GET", "POST"]) #The page where you can view the details of a game
def gameinfo():
    if request.method == "GET": # So people can only access it while logged in
        if 'user' in session and session['user']:
            return render_template("gameinfo.html")
        else:
            return redirect("/login/redirect")

@app.route("/create_item", methods=["GET", "POST"]) #The page for creating new items / editing item info
def create_item():
    if request.method == "GET": # So people can only access it while logged in
        if 'user' in session and session['user']:
            return render_template("create_item.html")
        else:
            return redirect("/login/redirect")

@app.route("/characters")
def characters():
    return render_template("character.html")

#---------------LOGIN Methods REGISTER + LOGOUT------------------------------
@app.route("/login", methods=["GET", "POST"])
@app.route("/login/<r>")
def login(r=None):
    if request.method == "GET": # What people see when they click "Login"
        if 'user' in session and session['user']:
            return redirect("/home")
        return render_template("login.html", r=r)
    else:
        form = request.form
        username = form['username'] or ""
        password = form['password'] or ""
        if utils.auth(username, password):
            session['user'] = username
            return 'success'
        return 'fail'

@app.route("/register", methods=["GET", "POST"]) # ----REGISTER-------
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

@app.route("/logout")#---------------------------LOGOUT--------------
def logout():
    session['user'] = None
    return redirect('/login')
#-----------------END LOGIN METHODS----------------------------------

if __name__ == "__main__":
    app.debug = True
    #app.secret_key = utils.secret_key
    app.run(port=8000)
