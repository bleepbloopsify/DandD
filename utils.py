from pymongo import MongoClient
import hashlib

secretkey= hashlib.md5("d&d").digest()

#-------------------ITEM METHODs-------------------
def makeItem(name, position=None, damage=None, armor=None, modifier=None, description=None):
    return 0# SHOULD INSERT INTO ENTITY INVENTORY





#----------------------Game GeT, SEt, make!----------------------
def setGame(idnum, players=[], enemies=[], npcs=[], map_location=""):
    return 0

def getGames(host): # Get a list of game names from this host(to be displayed in a tabel)
    names = ["Basement"]
    return names

def makeGame(host):
    # connection = MongoClient()
    # c = connection['data']
    # idnum = c.games.count() + 1
    # game = {
    #     'id':idnum,
    #     'host':
    # }

    return True
#-----------------END GAME EMTHODS-------------------------

#-------------------MORE LOGIN METHODS-----------------------------------------------
def auth(username, password):
    if username == "" or password == "":
        return False
    connection = MongoClient() #Connect to the Mongodb
    c = connection['data']
    print c.collection_names()
    print len(c.collection_names())
    if not "users" in c.collection_names():#Check if the table 'users' exists
       return False
    if not c.users.find_one({'username':username}):#Check the username
       return False
    if not hashlib.md5(password).hexdigest() ==  c.users.find_one({'username':username})['password']:#Check the password
       return False
    return True#If Password and Uname match return true

def register(username, password, confirm_password):
    print "hi"
    if username == "" or password == "" or confirm_password == "":
        return False
    #Connect to the Mongo DB
    connection = MongoClient()
    c = connection['data']
    #Check that the passwords are the same
    if not password == confirm_password:
        return False
    #Check that the username exists:
    if len(username) < 1:
        return False
    #Check that the password exists:
    if len(password) < 1:
        return False
    #Check if the username is taken
    if c.users.find_one({'username':username}) != None:
        return False
    #Encrypt Password
    encrypted = hashlib.md5(password).hexdigest()
    #Enter the information
    d = {
        'username': username,
         'password':encrypted,
         'dmgames':[],
         'pgames':[]
         }
    c.users.insert(d)
    return True
#----------------------------END MORE LOGIN METHODS------------------------------
