'''
use python3
'''

import query, db, word

q = query.Query();
print(q.getPageContentForLanguage("saada"));

'''
dataBase = db.DataBase();
dataBase.insertOneToCollection({"name": "mike", "age": 35}, "name-test");
'''

print(word.suffix_match("sattua", "vapua"));
print(word.suffix_match_vowels("satama", "sorava"));
print(word.suffix_match_vowels("syväille", "ensikymäille"));
