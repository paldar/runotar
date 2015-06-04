'''
use python3
'''

import pywikibot as pw, sys;

class Query:
    def __init__(self):
        self.site = pw.getSite();

    def getPageContent(self, title="olla"):
        page = pw.Page(self.site, title);
        pageContent = "";
        try:
            pageContent = page.get();
        except pw.exceptions.Error:
            pageCotent = "";
            sys.stderr.write("Page for " + title + " not found\n");
        return pageContent;
    def getPageContentForLanguage(self, title="olla", language="Finnish"):
        language = "=="+language.capitalize();
        queryResult = self.getPageContent(title);
        start = queryResult.find(language);
        end = queryResult.find("----",start);
        if (start != -1 and end!= -1):
            return queryResult[start:end];
        else:
            sys.stderr.write("Entry for " + title + " in " + language + " not found\n");
            return "";




