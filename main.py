'''
use python3
'''

import query, db

q = query.Query();
print(q.getPageContentForLanguage());

dataBase = db.DataBase();
dataBase.insertOneToCollection({"name": "mike", "age": 35}, "name-test");