#crawler:

import query, db, word, utils, multiprocessing, pywikibot as pw
from multiprocessing import Pool
from collections import deque

def crawlSpace(initWord="olla", language="Finnish", collectionName="name-test"):
    queryWord = initWord
    q = query.Query()
    dataBase = db.DataBase()
    wordObj = q.getWordEntryForLanguage(queryWord, language)
    if wordObj != None:
        dataBase.upsertOneToCollection(wordObj.toObject(), wordObj.hashValueDict, collectionName)
        queue = deque(q.linksIterator);
        while len(queue):
            link = queue.popleft()
            #this is bad...but hey....
            if isinstance(link, pw.Page):
                title = link._link.canonical_title()
                print(title)
                if ("Category" in title) and ("Finnish" in title):
                    #add links:
                    queue.extend(link.linkedPages());
                    print("added category")
                    continue
                if (title):
                    wordString = q.parseContentOfLanguage(title, q.getContentOfPage(link), language)
                    if len(wordString):
                        wordObj =  word.Word(title, language, wordString);
                        dataBase.upsertOneToCollection(wordObj.toObject(), wordObj.hashValueDict, collectionName)
                        queue.extend(q.linksIterator)

crawlSpace()
