#contains random utility functions

import random, string, re

#credit:
#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def generateRandomString(length):
    return ''.join(random.SystemRandom().choice(string.digits + string.ascii_letters) for _ in range(length))

def linkToPlainText(orig):
    pass


def removeUselessHTML(orig):
    replTags = ['class', 'style', 'colspan']
    for tag in replTags:
        orig = re.sub(tag+"=\".*\"","",orig,re.MULTILINE)
    orig = re.sub("\|[\s]*?\n", "", orig, re.MULTILINE)
    orig = re.sub("\|-(\s|.)*?\|", "", orig, re.MULTILINE)
    
    return orig