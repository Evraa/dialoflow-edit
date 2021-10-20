import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# also the database name
mydb = myclient["db2"]
USERS_OBJ = mydb['users'] #main collection object

result = (USERS_OBJ.find({'email':"haynesdonna@gmail.com"}))
have_list = True if len(list(result)) else False

print(have_list)

print ("*******************")
result = (USERS_OBJ.find({'email':"ev@gmail.com"}))
have_list = True if len(list(result)) else False

print(have_list)
