from pymongo import MongoClient
import hashlib

secretkey= hashlib.md5("d&d").digest()

#-------------------TEST METHODS------------------
def creategame(form):
    return "yay"#SEAN CAN YOU USE MAKE GAME AND SET GAME HERE THIS HAS ALL THE PARAMETERS FROM THE THING

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
def makeChar(username,name=None,race=None,subrace=None,hpmax=None,hpcurr=None,status=None,traits=None,items=None):
    #Connect to Mongodb
    connection = MongoClient()
    c = connection['data']
    #Find the correct characterid
    idnum = c.characters.count() + 1
    #Create the Character
    character = {
	'name':name,
	'race':race,
	'idnum':idnum,
	'subrace':subrace,
	'hpmax':hpmax,
	'hpcurr':hpcurr,
	'status':status,
	'traits':traits,
	'items':items
	}
    #Insert the Character into the Character collection and insert the character into the users list
    c.characters.insert(character)
    userchars = c.users.findone({'username':username})['characters']
    userchars.append(character)
    c.users.update({'username':username}, {"$set":{'characters':userchars}})

#Get Character Names
<<<<<<< HEAD
def getCharNames(user=None):#HAS TO RETURN CHARACTER STUFFS TOO
    if not user:
        return "Leon"
	#Connect to mongodb
	connection = MongoClient()
	c = connection['data']
	#Get every character
	cursor = c.characters.find()
	names =[]
	#Get Names
	for character in cursor:
		names.append(character)

=======
def getNames(username):
	#Connect to mongodb
	connection = MongoClient()
	c = connection['data']
	#Find the User and Get Names
	return c.users.find_one({'username':username})['characters']
>>>>>>> 49d7fbf3c588c2c1b7f35452e9aeefe9bd4074f7
#Modify preexisting characters
def updateChar(idnum,name=None,race=None,subrace=None,hpmax=None,hpcurr=None,status=None,traits=None,items=None):
	#Connect to Mongodb
	connection = MongoClient()
	c = connection['data']
	#Find the Character
	character = c.characters.find_one({'idnum':idnum})
	#Go through the information passed, if no info was passed leave as is
	new_char={
	'name':name or character['name'],
	'race': race or character['race'],
	'subrace': subrace or character['subrace'],
	'hpmax' : hpmax or character['hpmax'],
	'hpcurr' : hpcurr or character['hpcurr'],
	'status' : status or character['status'],
	'traits' : traits or character['traits'],
	'items' : items or character['items']
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
         'host':host
     }
     c.games.insert(game)
     return idnum
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
