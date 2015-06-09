
import defs
from defs import vowels as vowels
from defs import isWordLike as wordLike

class Word:
    def __init__(self, title, wordType):
        self.title = title;
        self.wordType = wordType;
    def __str__(self):
        return self.title

def storeWikiEntry(entryString):
    pass;

#simple parser:
def parseWikiEntry(entryString):
    stack = [];

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

def generateRandomWordlikeStrings(vowels, consonants, length, isWordLike=wordLike):
    pass

