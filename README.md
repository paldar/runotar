# runotar

This is a crawler based on pywikibot, crawls through wiktionary entries and 
stores entries of a particular language into a MongoDB database.

modify and run
``
$ python3 crawler.py
``
for the desired effects.

The first milestone is considered to be done.
Currently the code does the following:
- given a starting entry on wiktionary, BFS through the entire connected space in a thread pool.
- with a given searched entry, the wiki text is parsed and stored into a Mongo database.
- duplicates are merged and updated, if possible.
- enables search of longest matching word from the right side for any given word, supports both "all letters", "vowels only" and "consonants only" (for alliteration).
- Query supports either a single language or all languages.

***TODO:***
- ~~Query database for a list of visited words~~
- ~~multithreading with crawling~~
- ~~filter out categories that do not have given language name~~
- ~~skip all appendices~~
- ~~store set of visited words to avoid multiple repeated visit.~~
- ~~longest matching string from the right side~~

