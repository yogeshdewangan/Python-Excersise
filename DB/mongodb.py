from pymongo import MongoClient

client = MongoClient("Host","Port", "username", "password")
db_name ="Monaco"
db = client[db_name]
db.authenticate("mongouser","password")
collection = db["collection_name"]
collection.find_one({"name":"Yogesh"})
client.close()