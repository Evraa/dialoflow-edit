import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# also the database name
mydb = myclient["bb2"]
USERS_OBJ = mydb['users'] #main collection object

result = (USERS_OBJ.find({'email':"haynesdonna@gmail.com"}))
print(result[0])
print ("*******************")
result = (USERS_OBJ.find({'email':"ev@gmail.com"}))
print(result[0])
