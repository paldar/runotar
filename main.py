'''
use python3
'''

import query, db, word, utils

q = query.Query();
text = q.getPageContentForLanguage("rough", language= "English")

for i in text:
    print(text[i])
    #print(i)
#utils.removeUselessHTML(text)

#q.testFunc()

'''
dataBase = db.DataBase();
dataBase.insertOneToCollection({"name": "mike", "age": 35}, "name-test");

print(word.suffix_match("sattua", "vapua"));
print(word.suffix_match_vowels("satama", "sorava"));
print(word.suffix_match_vowels("syväille", "ensikymäille"));
'''

#print(list(word.parseWikiEntry(q.getPageContent("olla")).keys()))