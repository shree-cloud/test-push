import pymongo

client = pymongo.MongoClient("mongodb+srv://shree:haonabhai@cluster0.i1peq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "shreyash",
    "surname": "Mohod",
    "email": "shree@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)