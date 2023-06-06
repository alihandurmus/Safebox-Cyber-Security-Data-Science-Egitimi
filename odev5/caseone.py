import random
import string

import pymongo


connection = pymongo.MongoClient("mongodb://localhost:8080")
db = connection['flaskmongodb']
UsersCollection = db['Users']
for i in range(50):
    random_data = {
        "name": ''.join(random.choices(['Alihan','Yusuf','Ahmet','Oguzhan','Ayse','Fatma','Asude','Murat','Can','Sena','Melike','Yakuphan','Mustafa'])),
        "age": random.randint(18, 65),
        "Job": random.choice(['engineer', 'teacher', 'doctor', 'artist', 'writer']),
        "Description" : 1


    }
    UsersCollection.insert_one(random_data)


