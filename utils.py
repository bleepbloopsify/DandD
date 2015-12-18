from pymongo import MongoClient
from hashlib import md5

secretkey= "asdfghhjkl"

def auth(username, password):    
   #Connect to the Mongodb
   connection = MongoClient()
   c = connection['data']
   #Check if the table 'users' exists
   if not "users" in c.collection_names():
       return False
   #Check the username
   if not c.users.find_one({'username':username}):
       return False
   #Check the password
   if not hashlib.md5(password) ==  c.users.find_one({'username':username})['password']:
       return False
   #If Password and Uname match return true
   return True

def register(username, password, confirm_password):
    #Connect to the Mongo DB
    connection = MongoClient()
    c = connection['data']
    #Check that the passwords are the same
    if not password == confirm_password:
        return "Passwords do not match"
    #Check that the username exists:
    if len(username) < 1:
        return "Invalid Username"
    #Check that the password exists:
    if len(password) < 1:
        return "Invalid Password"
    #Check if the username is taken
    if c.users.find_one({'username':username}) != None:
        return "Username already taken"
    #Encrypt Password
    encrypted = hashlib.md5(password)
    #Enter the information
    d = {'username': username,
         'password':encrypted,
         }
    c.users.insert(d)
    return None

def login(username, password):
    return False
