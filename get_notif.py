import pymongo
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python_test"]
# db = Connection().my_db
coll = mydb['test2']
cursor = coll.find(cursor_type=pymongo.CursorType.TAILABLE)
count = 0
while cursor.alive:
    # print('sasas')
    try:
        new_count = cursor.count()
        if new_count > count:
            count = new_count
            print('ini dia: ', new_count)
        # print(doc)
        # print('getting trigger')
    except StopIteration:
        time.sleep(1)
        print('stop itteration')