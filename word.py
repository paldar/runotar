
import defs, re, time
from defs import *

class Word:
    def __init__(self, title, language, parsedDictionary={}):
        self.title = title;
        self.language = language;
        self.content = parsedDictionary;
        self.content["title"] = title;
        self.content["language"] = language;
        self.hashValueDict = {"hashValue" :title+language};
        self.content["hashValue"] = title+language;
        self.wordTypes = [val for val in defs.wordTypes if val in parsedDictionary.keys()];
        self.content["type"] = self.wordTypes;

    def __str__(self):
        return self.title;

    def toObject(self):
        self.content["modifiedTime"] = time.time()
        return self.content

def deserializeJSONWordObject(parsedDictionary):
    return Word(parsedDictionary["title"],parsedDictionary["language"],parsedDictionary)

#simple parser:
def parseWikiEntry(entryString):
    langdict = {};
    lastindex = 0;
    while(lastindex < len(entryString)):
        regexMatch = re.search("^==[A-Z][a-z]+==(\s|.)*?(----|\Z)", entryString[lastindex:], re.MULTILINE)
        if(regexMatch):
            #hardcoded:
            language = (re.search("^==[A-Z][a-z]+==",regexMatch.group(0)).group(0)[2:-2]);
            trailingChars = len(regexMatch.groups()[-1])
            langdict[language] = parseSectionEntry(entryString[lastindex+regexMatch.start(0):lastindex+regexMatch.end(0)-trailingChars])
            lastindex += (regexMatch.end(0) - trailingChars)
        else:
            break
    return langdict

def parseSectionsAndSubsections(entryString, delimiter, subsectionFunction, discardNonMatchingInfo = True):
    secDict = {};
    lastindex = 0;
    while(lastindex < len(entryString)):
        regexMatch = re.search("^"+delimiter+"[A-Z][a-z]+"+delimiter+"[^=](\s|.)*?(^"+delimiter+"[A-Z]|\Z)", entryString[lastindex:], re.MULTILINE)
        if(regexMatch):
            #hardcoded:
            type = (re.search("^"+delimiter+"[A-Z][a-z]+"+delimiter,regexMatch.group(0)).group(0)[len(delimiter):-1*len(delimiter)]);
            trailingChars = len(regexMatch.groups()[-1])
            secDict[type] = subsectionFunction(entryString[lastindex+regexMatch.start(0):lastindex+regexMatch.end(0)-trailingChars])
            if lastindex==0 and regexMatch.start(0)>0:
                secDict["content"]=entryString[0:regexMatch.start(0)]
            lastindex += (regexMatch.end(0) - trailingChars)
        else:
            if lastindex==0:
                secDict["content"]=entryString;
            break
    return secDict

def parseSectionEntry(entryString):
    return parseSectionsAndSubsections(entryString, "===", parseSubSectionEntry)


def parseSubSectionEntry(entryString):
    return parseSectionsAndSubsections(entryString, "====", lambda x:x)

#hamming distance from wikipedia
#url: https://en.wikipedia.org/wiki/Hamming_distance
def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

#there's gotta be a better way to do this...
def suffix_match(a, b):
    a = list(reversed(list(str(a).lower())));
    b = list(reversed(list(str(b).lower())));
    matched_letters = 0;
    for i in range(len(a)):
        if i >= len(b):
            break;
        if a[i] == b[i]:
            matched_letters += 1;
        else:
            break;
    return matched_letters;

#modify vowel def when needed.
def suffix_match_vowels(a, b):
    a = list(reversed(list(str(a).lower())));
    b = list(reversed(list(str(b).lower())));
    matched_vowels = 0;
    for i in range(len(a)):
        if i >= len(b):
            break;
        if a[i] == b[i] and (a[i] in vowels):
            matched_vowels += 1;
        elif (a[i] in vowels) or (b[i] in vowels):
            break;
        else:
            #still counts, for ranking purposes
            matched_vowels += 1;
            continue;
    return matched_vowels;
#input: list
def rankBySuffix(words, target):
    return sorted(words, key = lambda word: suffix_match(word, target));
