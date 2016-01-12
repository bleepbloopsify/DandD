from pymongo import MongoClient
import hashlib

secretkey= hashlib.md5("d&d").digest()

#-------------------TEST METHODS------------------
def creategame(form):
    #First Make the Game and get the idnum
    idnum = makeGame(form['user'])
    #Set the Game
    setGame(idnum, form['players'])
    return idnum

#-------------------ITEM METHODs-------------------
def makeItem(charid, name,item_class, position=None, damage=None, armor=None, modifier=None, description=None):
    #Create the item
    item = {
        'name':name,
        'item_class':item_class,
        'position':position,
        'damage':damage,
        'armor':armor,
        'modifier':modifier,
        'description':description
        }
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the correct character and Add the item to their inventory
    old_inven = c.characters.find_one({'idnum':charid})['items']
    old_inven.append(item)
    c.characters.update({'idnum':charid},{"$set":{'items':old_inven}})

def rmvItem(charid, name):
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the Character and get his inventory
    inven = c.characters.find_one({'idnum':charid})['items']
    #Iterate over the inventory and find and remove the correct item
    for item in items:
        if (item['name'] == name):
            items.remove(item)
            break
    #Update the Character Inventory
    c.characters.update({'idnum':charid}, {"$set":{'items':inven}})
#----------------------Character Methods-------------------------
#Create a prelim char and attach it to a username
def createChar(form):
    print "go"
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the correct characterid
    idnum = c.characters.count() + 1
    #Create the Character
    character = {
    'name':form['charname'] or "",
    'race':form['race'] or "",
    'idnum':idnum,
    'subrace':form['subrace'] or "",
    #'hpmax':form['hpmax'] or "",
    #'hpcurr':form['hpcurr'] or "",
    #'status':form['status'] or "",
    #'traits':form['traits'] or "",
    #'items':form['items'] or ""
    }
    #Insert the Character into the Character collection and insert the character into the users list
    c.characters.insert(character)
    userchars = c.users.find_one({'username':form['user']})['characters']
    userchars.append(character)
    c.users.update({'username':form['user']}, {"$set":{'characters':userchars}})
    return idnum

#Remove Characters
#def rmvChar(idnum,username=None,gameid=None):
    #Connect to Mongo
  #  connection = MongoClient()
  #  c = connection['data']
    #If username was passed, check if the username is correct for the character
  #  if username != None:
        #Check if username is in database
  #      cursor  = c.users.find()
  #      for user in cursor:
   #         if username == user['username']:
                #If the name exists, then get all the characters from the user
   #             charlist = c.users.find_one({'username':username})['characters']
                #Check if 
        
#Get Character Names
def getNames(username=None):
    #Connect to mongodb
    connection = MongoClient()
    c = connection['data']
    #IF no param
    if not username:
        cursor= c.characters.find()
        names = {}
        for char in cursor:
            names[char['idnum']] = char
        return names
    print username
    #Find the User and Get Names
    chars = c.users.find_one({'username':username})['characters']
    print chars
    names = {}
    for char in chars:
        names[char['idnum']]= char
    return names

#Modify preexisting characters
def updateChar(form):
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the Character
    character = c.characters.find_one({'idnum':form['idnum']})
    #Go through the information passed, if no info was passed leave as is
    new_char={
    'name':form['name'] or character['name'],
    'race': form['race'] or character['race'],
    'subrace': form['subrace'] or character['subrace'],
    'hpmax' : form['hpmax'] or character['hpmax'],
    'hpcurr' : form['hpcurr'] or character['hpcurr'],
    'status' : form['status'] or character['status'],
    'traits' : form['traits'] or character['traits'],
    'items' : form['items'] or character['items']
    }
    #Update the Character
    c.characters.update({'idnum':idnum}, new_char)
#----------------------Game GeT, SEt, make!----------------------
def setGame(idnum, players=[], enemies=[], npcs=[], map_location=""):
    #Setup connection
    connection = MongoClient()
    c = connection['data']
    #Check if the idnum is valid
    if not c.games.find_one({'id':idnum}):
        return False
    #Get the correct game
    game = c.games.find_one({'id':idnum})
    #Go through the information passed, If no new info was passed, set it to the previous version
    new_players = players or game['players']
    new_enemies = enemies or game['enemies']
    new_npcs = npcs or game['npcs']
    new_map_location = map_location or game['map_location']
    #Change the old values to the new ones
    c.games.update({'id':idnum}, {"$set":{'players':new_players, 'enemies':new_enemies, 'npcs':new_npcs, 'map_location':new_map_location}})
    return True

def getGames(host): # Get a list of game names from this host(to be displayed in a tabel)
    connection = MongoClient()
    c = connection['data']
    #Check if the host is in the games db
    if not c.games.find_one({'host':host}):
        return False
    #Create the list to hold the game names
    names = []
    #Loop through users and find the correct users games
    names = c.users.find_one({'users':host})['dmgames']
    #Return the list
    return names

def makeGame(host):
     connection = MongoClient()
     c = connection['data']
     idnum = c.games.count() + 1
     game = {
         'id':idnum,
         'host':host,
     }
     c.games.insert(game)
     return idnum
#-----------------END GAME EMTHODS-------------------------

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
         'games':[],
         'characters':[]
         }
    c.users.insert(d)
    return True
#----------------------------END MORE LOGIN METHODS------------------------------
