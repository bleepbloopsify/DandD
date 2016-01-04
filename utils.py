from pymongo import MongoClient
import hashlib

secretkey= hashlib.md5("d&d").digest()

#-------------------ITEM METHODs-------------------
def makeItem(gameid,charid, name,item_class, position=None, damage=None, armor=None, modifier=None, description=None):
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
    characterlist = c.games.find_one({'id':gameid})['players']
    for character in characterlist:
        if character['idnum'] == charid:
            character['items'][item_class].append(item)
            break
    #Update the players list
    c.games.update({'id':gameid},{'$set':{'players':characterlist}})

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
    #Loop through games and find all the games with host = host
    cursor = c.games.find({'host':host})
    for game in cursor:
        names.append(game['name'])
    #Return the list
    return names

def makeGame(host):
     connection = MongoClient()
     c = connection['data']
     idnum = c.games.count() + 1
     game = {
         'id':idnum,
         'host':host
     }
     c.games.insert(game)
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
         'games':[]
         }
    c.users.insert(d)
    return True
#----------------------------END MORE LOGIN METHODS------------------------------
