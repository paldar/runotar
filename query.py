'''
use python3
'''

import pywikibot as pw, sys;
import word, mwparserfromhell as mp

class Query:
    def __init__(self):
        self.site = pw.getSite();

    def getPageContent(self, title="olla"):
        page = pw.Page(self.site, title);
        try:
            self.rawPageText = page.get();
            #do not expand templates for now
            self.linksIterator = page.linkedPages();
            return mp.parse(pw.textlib.removeHTMLParts(
                      pw.textlib.removeLanguageLinksAndSeparator(
                         pw.textlib.removeCategoryLinksAndSeparator(self.rawPageText)), keeptags=[]));
        except pw.exceptions.Error:
            sys.stderr.write("Page for " + title + " not found\n");
            return ""

    def getPageContentForLanguage(self, title="olla", language="Finnish"):
        # use word's parser:
        self.entryDict = word.parseWikiEntry(self.getPageContent(title))
        if language.capitalize() in self.entryDict.keys():
            return self.entryDict[language.capitalize()]
        else:
            sys.stderr.write("Entry for " + title + " in " + language + "== not found\n");
            return "";