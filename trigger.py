import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python_test"]

# mycol = mydb.create_collection('test2', capped=True, size=2)