'''
use python3
'''

import query, db, word, utils

q = query.Query();
word = q.getWordEntryForLanguage("olla", language= "Finnish")

dataBase = db.DataBase();
dataBase.upsertOneToCollection(word.toObject(), word.hashValueDict, "name-test");
'''
print(word.suffix_match("sattua", "vapua"));
print(word.suffix_match_vowels("satama", "sorava"));
print(word.suffix_match_vowels("syväille", "ensikymäille"));
'''

#print(list(q.linksIterator))

#print(list(word.parseWikiEntry(q.getPageContent("olla")).keys()))
