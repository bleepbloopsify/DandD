from pymongo import MongoClient
from hashlib import md5

secretkey= "asdfghhjkl"

def auth(username, password):
    if username == "DM" and password == "DandD":
        return True
    else:
        return False

