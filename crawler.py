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


def queryAndReturnNeighbors(page, collection, visitedSet, language):
    if not isinstance(page, pw.Page):
        return set()
    #return empty set:
    q = query.Query()
    title = page._link.canonical_title()
    if title in visitedSet:
        return set()
    else:
        print(title)
        if ("Category" in title and language in title):
            #add links:
            print("added category")
            return set(page.linkedPages())
        elif ("Appendix" in title):
            return set()
        else:
            wordString = q.parseContentOfLanguage(title, q.getContentOfPage(page), language)
            if len(wordString):
                wordObj =  word.Word(title, language, wordString);
                dataBase.upsertOneToCollection(wordObj.toObject(), wordObj.hashValueDict, collectionName)
                return set(q.linksIterator)
            else:
                return set()


def crawlSpace2(initWord="olla", language="Finnish", collectionName="finnish"):
    dataBase = db.DataBase()
    visitedSet = set(dataBase.getAllVisitedTitles(collectionName))

