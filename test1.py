import pymongo
client = pymongo.MongoClient("mongodb+srv://mayank:mayank@cluster0.trwkkyl.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"mayank",
    "email":"mayank@gmail.com",
    "surname":"joshi"
}
d = {
    "name":"mayank",
    "email":"mayank@gmail.com",
    "surname":"joshi"
}
d = {
    "name":"mayank",
    "email":"mayank@gmail.com",
    "surname":"joshi"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)