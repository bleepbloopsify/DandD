from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit
import utils

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.secret_key = utils.secretkey
socketio = SocketIO(app)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route('/games', methods=['GET', "POST"])# Page for viewing the list of all of your games
def games():
    if request.method == "GET":
        if 'user' in session and session['user']:
            return render_template("games.html")
        else:
            return redirect("/login/redirect")
    elif request.method == "POST":
        user = request.form['user']
        return utils.getGames(user)

@app.route('/creategame', methods=['GET','POST'])
def creategame():
    if request.method == "POST":
        form = request.form
        form['user'] = session['user']
        return utils.creategame(form)
    else:
        return redirect("/games")

@app.route("/gameinfo")
@app.route("/gameinfo/<id>", methods=["GET", "POST"]) #The page where you can view the details of a game
def gameinfo(id=0):
    if id == 0:
        return redirect("/games")
    if request.method == "GET": # So people can only access it while logged in
        if 'user' in session and session['user']:
            return render_template("gameinfo.html")
        else:
            return redirect("/login/redirect")
    else:
        form = request.form

@app.route("/characters", methods=['GET', 'POST'])
def characters():
    if request.method == 'GET':
        charsSent = utils.getNames()
        return render_template("character.html",charsSent=charsSent)
    else:
        form = request.form
        form['user'] = session['user']
        return utils.createChar(form)

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

#------------------------------SOCKET METHODS FOR GAMEINFO-----------------
@socketio.on('connected')
def connected(packet):
    print packet['data']

@socketio.on('clicked!!!')
def clicked(packet):
    print packet['data'], "\n"
    pass

#------------------------------- END SOCKET METHODS-----------------------



if __name__ == "__main__":
    app.debug = True
    #app.secret_key = utils.secret_key
    socketio.run(app, port=8000)
