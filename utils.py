from pymongo import MongoClient
import hashlib
import json

secretkey= hashlib.md5("d&d").digest()

#-------------------TEST METHODS------------------


#-------------------ITEM METHODs-------------------
def makeItem(charid,form):
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the correct character and Add the item to their inventory
    old_inven = c.characters.find_one({'idnum':charid})['items']
    old_inven.append(form)
    c.characters.update({'idnum':charid},{"$set":{'items':old_inven}})

def updateItem(charid, form):
    #Connect to Mongo db
    connection = MongoClient()
    c = connection['data']
    #Update the item
    old_inven = c.characters.find_one({'idnum':charid})['items']
    for item in old_inven[form['subtype']]:
        if item['id'] == form['id']:
            index = old_inven[form['subtype']].index(item)
            old_inven[form['subtype']][index] = form
            break
    #Update Inventory
    c.characters.update({'idnum':charid},{"$set":{'items':old_inven}})

def rmvItem(charid,form):
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the Character and remove the item from his inventory
    inven = c.characters.find_one({'idnum':charid})['items']
    inven[form['subtype']].pop(inven[form['subtype']].index(form))
    #Update the Character Inventory
    c.characters.update({'idnum':charid}, {"$set":{'items':inven}})
#----------------------Character Methods-------------------------
#Create a prelim char and attach it to a username
def createChar(form):
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the correct characterid
    idnum = c.characters.count() + 1
    form['idnum'] = idnum
    #Insert the Character into the Character collection and insert the character into the users list
    c.characters.insert(form)
    userchars = c.users.find_one({'username':form['user']})['characters']
    userchars.append(idnum)
    c.users.update({'username':form['user']}, {"$set":{'characters':userchars}})
    return idnum

#Remove Characters
def rmvChar(idnum,username=None,gameid=None):
    #Connect to Mongo
    connection = MongoClient()
    c = connection['data']
    #If username was passed, check if the username is correct for the character
    if username != None:
        userchars = c.users.find_one({'username':username})['characters']
        for x in userchars:
            if x['idnum']==idnum:
                userchars.remove(x)
                c.users.update({'username':username},{"$set":{'characters':userchars}})
                #Go through games and remove the character from any games
                cursor = c.games.find()
                for game in cursor:
                    if idnum in game['players']:
                        game['players'].remove(idnum)
                        c.games.update({'id':game['id']},{"$set":{'players':game['players']}})
                c.characters.delete_one({'idnum':idnum})
    #If no username was passed but a gameid was passed, go to that game and remove the character
    elif gameid != None:
        game = c.games.find_one({'id':gameid})
        game['players'].remove(idnum)
        c.games.update({'id':game['id']},{"$set":{'players':game['players']}})
    #Else just remove the idnum from all games
    else:
        cursor = c.games.find()
        for game in cursor:
            if idnum in game['players']:
                game['players'].remove(idnum)
                c.games.update({'id':game['id']},{"$set":{'players':game['players']}})

#Get Character by Idnum
def getChar(idnum):
    connection = MongoClient()
    c = connection['data']
    return c.characters.find_one({'idnum':int(idnum)})

#Get all characters associated with an account
def getChars(username=None):
    #Connect to mongodb
    connection = MongoClient()
    c = connection['data']
    if username:
        charids = c.users.find_one({'username':username})['characters']
        characters = {}
        for id in charids:
            characters[id] = c.characters.find_one({'idnum':id})
        for character in characters:
            characters[character].pop("_id")
        return characters
    else:
        return c.characters.find()
    #IF no param
    if not username:
        cursor= c.characters.find()
        names = {}
        for char in cursor:
            names[char['idnum']] = char
        return names
    #Find the User and Get Names
    chars = c.users.find_one({'username':username})['characters']
    names = {}
    for char in chars:
        names[char['idnum']]= char
    return names

#Modify a single character by id number
def updateChar(idnum, form):
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Update the Character
    c.characters.update({'idnum':idnum}, {"$set":form})
#----------------------Game GeT, SEt, make!----------------------
#INITIALIZE A GAME
def creategame(form):
    #First Make the Game and get the idnum
    idnum = makeGame(form['user'])
    #Set the Game
    setGame(idnum, form)
    return str(idnum)

#OUTLINE GAME
def makeGame(host):
    connection = MongoClient()
    c = connection['data']
    idnum = c.games.count() + 1
    game = {
    'id':idnum,
    'host':host,
    }
    c.games.insert(game)
    #Add the game to the hosts dmgames
    ugames = c.users.find_one({'username':host})['dmgames']
    ugames.append(game['id'])
    c.users.update({'username':host},{"$set":{'dmgames':ugames}})
    return idnum

# Change the game
def setGame(idnum, form):
    #Setup connection
    idnum = int(idnum)
    connection = MongoClient()
    c = connection['data']
    #Check if the idnum is valid
    if not c.games.find_one({'id':idnum}):
        return False
    #Get the correct game
    game = c.games.find_one({'id':idnum})
    #Go through the information passed, If no new info was passed, set it to the previous version
    #Change the old values to the new ones
    c.games.update({'id':idnum}, {"$set":form})
    return True

def updateGame(idnum, form):
    #Setup connection
    idnum = int(idnum)
    connection = MongoClient()
    c = connection['data']
    #Check if the idnum is valid
    if not c.games.find_one({'id':idnum}):
        return False
    #Get the correct game
    game = c.games.find_one({'id':idnum})
    #Go through the information passed, If no new info was passed, set it to the previous version
    #Change the old values to the new ones
    print form
    c.games.replace_one({'id':idnum}, form)
    return True


#Add player to game by id
def addPlayer(host, gameid, charid):
    #Setup connection
    connection = MongoClient()
    c = connection['data']
    #Check if the host id is correct
    if not c.games.find_one({'id':gameid})['host'] == host:
	return False
    #Check if the character exists
    if not c.characters.find_one({'idnum':charid}):
	return False
    #If id is correct, add the characters id to games and add the gameid to pgames
    players = c.games.find_one({'id':gameid})['players']
    players.append(charid)
    c.games.update({'id':gameid},{"$set":{'players':players}})
    #Find the player that made the character
    pcharname = c.characters.find_one({'idnum':charid})['user']
    pgames = c.users.find_one({'username':pcharname})['pgames']
    pgames.append(gameid)
    c.users.update({'username':pcharname},{"$set":{'pgames':pgames}})

#Gets all games associated with user=host
def getGames(host): # Get a list of game names from this host(to be displayed in a tabel)
    connection = MongoClient()
    c = connection['data']
    #Check if the host is in the games db
    if not c.games.find_one({'host':host}):
        return False
    #Create the list to hold the game names
    names = []
    #Loop through users and find the correct users games
    names = c.users.find_one({'username':host})['dmgames']
    #With the list of ids, get all the corresponding games
    games = []
    for name in names:
        games.append(c.games.find_one({'id':name}))
    for game in games:
        if game and game['_id']:
            game.pop('_id')
    return games

def getGame(idnum):
    connection= MongoClient()
    c = connection['data']
    game = c.games.find_one({'id':int(idnum)})
    if not game:
        return False
    game.pop("_id")
    return game
#-----------------END GAME MeTHODS-------------------------

#-----------------User Methods-----------------------------
def update_pw(user,old_password, new_password):
    #Connect to Mongo
    connection = MongoClient()
    c = connection['data']
    #Find the old password
    password = c.users.find_one({'username': user})['password']
    #Get the password encryption
    encrypted_old = hashlib.md5(old_password).hexdigest()
    #Check if the old passwords match
    if not encrypted_old == password:
        return False
    #If the passwords match, Encrypt the new password and set the password
    encrypted_new = hashlib.md5(new_password).hexdigest()
    c.users.update({'username':user}, {"$set":{'password':encrypted_new}})
    return True

def update_user(old_user, new_user, password):
    #Connect to Mongo
    connection = MongoClient()
    c = connection['data']
    #Get the password
    pw = c.users.find_one({'username':old_user})['password']
    #Check if the passwords are the same
    if not hashlib.md5(password).hexdigest() == pw:
        return False
    #If the passwords match, update the username in users
    c.users.update({'username':old_user}, {"$set":{'username':new_user}})
    #Get all the games that the user is hosting and update the list of players
    c.games.update({'host':old_user},{"$set":{'host':new_user}})
    return True

#-------------------MORE LOGIN METHODS-----------------------------------------------
def auth(username, password):
    if username == "" or password == "":
        return False
    connection = MongoClient() #Connect to the Mongodb
    c = connection['data']
    if not "users" in c.collection_names():#Check if the table 'users' exists
       return False
    if not c.users.find_one({'username':username}):#Check the username
       return False
    if not hashlib.md5(password).hexdigest() ==  c.users.find_one({'username':username})['password']:#Check the password
       return False
    return True#If Password and Uname match return true

def register(username, password, confirm_password):
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
	 'pgames':[],
         'characters':[]
         }
    c.users.insert(d)
    return True
#----------------------------END MORE LOGIN METHODS------------------------------
