'''
use python3
'''

import pywikibot as pw, sys;

class Query:
    def __init__(self):
        self.site = pw.getSite();

    def getPageContent(self, title="olla"):
        page = pw.Page(self.site, title);
        try:
            self.rawPageText = page.get();
            self.linksIterator = page.linkedPages();
            return pw.textlib.removeHTMLParts(pw.textlib.removeLanguageLinksAndSeparator(pw.textlib.removeCategoryLinksAndSeparator(page.expand_text())), keeptags=['tt', 'nowiki']);
        except pw.exceptions.Error:
            sys.stderr.write("Page for " + title + " not found\n");
            return ""

    def getPageContentForLanguage(self, title="olla", language="Finnish"):
        queryResult = self.getPageContent(title);
        if not pw.textlib.does_text_contain_section(queryResult, language):
            raise Exception('language not found')
        language = "=="+language.capitalize();
        start = queryResult.find(language);
        end = queryResult.find("----",start);
        if (start != -1 and end == -1):
            end = len(queryResult);
        if (start != -1 and end!= -1):
            return queryResult[start:end];
        else:
            sys.stderr.write("Entry for " + title + " in " + language + "== not found\n");
            return "";

    def testFunc(self):
        page = pw.Page(self.site, "saada");
        '''
        print(page.get());
        print(page.section());
        for i in page.backlinks():
            print(i)
        for i in page.linkedPages():
            print(i)
        for i in page.categories():
            print(i)
        print(page.expand_text())
            '''
        print(pw.textlib.does_text_contain_section(page.expand_text(), "Finnish"))
        text = pw.textlib.removeCategoryLinksAndSeparator(page.get());
        text = pw.textlib.removeLanguageLinksAndSeparator(text)


