'''
use python3
'''

import pywikibot as pw, sys;
import word, mwparserfromhell as mp

class Query:
    def __init__(self):
        self.site = pw.getSite();

    def getContentOfPage(self, page):
        try:
            self.rawPageText = page.get();
            #do not expand templates for now
            self.linksIterator = page.linkedPages();
            return mp.parse(pw.textlib.removeHTMLParts(
                      pw.textlib.removeLanguageLinksAndSeparator(
                         pw.textlib.removeCategoryLinksAndSeparator(self.rawPageText)), keeptags=[]));
        except:
            sys.stderr.write("Page for " + page._link.canonical_title() + " not found\n");
            return ""

    def getPageContent(self, title="olla"):
        page = pw.Page(self.site, title);
        return self.getContentOfPage(page)

    def getPageContentForLanguage(self, title="olla", language="Finnish"):
        return self.parseContentOfLanguage(title, self.getPageContent(title), language)

    def parseContentOfLanguage(self, title, content, language):
        if language.capitalize() in content:
            # use word's parser:
            self.entryDict = word.parseWikiEntry(content)
            if language.capitalize() in self.entryDict.keys():
                return self.entryDict[language.capitalize()]
            else:
                sys.stderr.write("Entry for " + title + " in " + language + " not found\n");
                return "";
        else:
            sys.stderr.write("Entry for " + title + " in " + language + " not found\n");
            return ""

    #returns a word object
    def getWordEntryForLanguage(self, title="olla", language="Finnish"):
        rawString = self.getPageContentForLanguage(title,language);
        if len(rawString):
            return word.Word(title, language, rawString);
        else:
            return None
