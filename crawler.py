#crawler:

import query, db, word, utils, multiprocessing, pywikibot as pw
from concurrent.futures import ThreadPoolExecutor as Executor
from collections import deque

def crawlSpace(initWord="olla", language="Finnish", collectionName="finnish"):
    queryWord = initWord
    visitedSet = set()
    q = query.Query()
    dataBase = db.DataBase()
    wordObj = q.getWordEntryForLanguage(queryWord, language)
    visitedSet.add(initWord)
    if wordObj != None:
        dataBase.upsertOneToCollection(wordObj.toObject(), wordObj.hashValueDict, collectionName)
        queue = deque(q.linksIterator);
        while len(queue):
            link = queue.popleft()
            #this is bad...but hey....
            if isinstance(link, pw.Page):
                title = link._link.canonical_title()
                print(title)
                if ("Category" in title):
                    if ("Finnish" in title):
                        #add links:
                        queue.extend(link.linkedPages());
                        print("added category")
                    continue
                elif ("Appendix" in title):
                    continue
                elif (title in visitedSet):
                    continue
                elif (title):
                    wordString = q.parseContentOfLanguage(title, q.getContentOfPage(link), language)
                    if len(wordString):
                        wordObj =  word.Word(title, language, wordString);
                        visitedSet.add(title)
                        dataBase.upsertOneToCollection(wordObj.toObject(), wordObj.hashValueDict, collectionName)
                        queue.extend(q.linksIterator)


def crawlSpace2(initWord="olla", language="Finnish", collectionName="finnish"):
    visitedSet = set()
    q = query.Query()
    dataBase = db.DataBase()