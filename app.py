from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit
import utils
import json

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.secret_key = utils.secretkey
socketio = SocketIO(app)

#-------------------HOME PAGE------------
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")
#---------------------END HOME PAGE----------

#---------------GAME MASTER METHODS----------------
@app.route('/games', methods=['GET', "POST"])# Page for viewing the list of all of your games
def games():
    if request.method == "GET":
        if 'user' in session and session['user']:
            games = utils.getGames(session['user'])
            games = json.dumps(games)
            return render_template("games.html", games = games)
        else:
            return redirect("/login/redirect")
    elif request.method == "POST":
        user = request.form['user']
        return json.dumps(utils.getGames(user))

@app.route('/getgame')
def getgame():
    if 'user' in session and session['user']:
        return json.dumps(utils.getGames(session['user']))
    else:
        return redirect("/home")

@app.route('/creategame', methods=['GET','POST'])
def creategame():
    if request.method == "POST":
        form = request.form.copy().to_dict()
        form['user'] = session['user']
        print form
        return utils.creategame(form)
    else:
        return redirect("/games")


@app.route("/gameinfo")
@app.route("/gameinfo/<id>", methods=["GET", "POST"]) #The page where you can view the details  a game
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
#----------------END GAME MASTER METHODS---------------

#------------CHARACTER PAGE METHODS--------------------
@app.route("/characters", methods=['GET', 'POST'])
def characters():
    if request.method == 'GET':
        if 'user' in session and session['user']:
            names = utils.getChars(session['user'])
            for name in names:
                names[name].pop('_id',None)
            names = json.dumps(names)
            print names
            return render_template("character.html", sentChars=names)
        else:
            return redirect("/login/redirect")
    else:
        form = request.form.copy().to_dict()
        form['user'] = session['user']
        answer = utils.createChar(form)
        return str(answer)

@app.route("/getchars", methods=["POST"])
def getchars():
    if request.method == "POST":
        names = utils.getChars(session['user'])
        print str(names)
        return str(names)

@app.route("/charinfo")
@app.route("/charinfo/<id>", methods=["GET", "POST"])
def charinfo(id=0):
    if id == 0:
        return redirect("/characters")
    if request.method == "GET":
        if 'user' in session and session['user']:
            return render_template("charinfo.html")
        else:
            return redirect("/login/redirect")
    else:
        char = utils.getChar(id)
        char.pop('_id')
        return json.dumps(char)
#-------------END CHARACTER METHODS-----------------


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
        form = request.form.copy().to_dict()
        username = form['username'] or ""
        password = form['password'] or ""
        confmpwd = form['confmpwd'] or ""
        if utils.register(username, password, confmpwd):
            session['user'] = username
            return 'success'
        return 'fail'

@app.route("/editaccount", methods=['GET', 'POST'])
def editaccount():
    if request.method == 'GET':
        if 'user' in session and session['user']:
            return render_template("editaccount.html")
        else:
            return redirect("/login/redirect")
    else:
        form = request.form.copy().to_dict()
        username = session['user']
        newusername = form['newUsername'] or ""
        newpassword = form['newPassword'] or ""
        oldpassword = form['oldPassword']

        if form['newUsername'] and form['newPassword']:
            if utils.update_user(username,newusername,oldpassword):
                if utils.update_pw(newusername,oldpassword,newpassword):
                    return 'bothSuccess'
            return 'fail'

        if form['newUsername']:
            if utils.update_user(username,newusername,oldpassword):
                return 'userSucess'
            return 'fail'
            
        if form['newPassword']:
            if utils.update_pw(username,oldpassword,newpassword):
                return 'pwSuccess'
            return 'fail'
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


#-----------RUN--------------
if __name__ == "__main__":
    app.debug = True
    #app.secret_key = utils.secret_key
    socketio.run(app, port=8000)
