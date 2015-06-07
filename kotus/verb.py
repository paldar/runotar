'''
this conjugation module is reverse engineered based on the results from wiktionary.
I suppose there's an open sourced version of something like this lying around somewhere
but I'm too lazy to search for it :)
plus I can probably remember how to conjugate these words by doing this.
'''

import os, sys
import defs.vowels as vowels
import defs.vowelHarmonyDict as vowelHarmonyDict


personalEndings = ['n', 't', '', 'mme', 'tte', 'vat']

#special cases:
negationVerb = ['en', 'et', 'ei', 'emme', 'ette', 'eivät']

#list with ref from http://www.uusikielemme.fi/consonantgradation.html
gradationDict = {
    "nt":"nn", #nt->nn
    "k":"", #k->""
    "k":"v", #k->v
    "t":"d",
    "p":"v",
    "kk":"k",
    "pp":"p",
    "tt":"t",
    "nk":"ng",
    "lt":"ll",
    "rt":"rr",
    "mp":"mm",
    "lki":"lje",
    "rki":"rje"
}

gradationTypeOne = {
    "nt":"nn",
    "k":"", #k->""
    "kk":"k",
    "tt":"t",
    "t":"d",
    "rt":"rr",
}
#type 52: sanoa
def conjugate52(stem):
    #c: short for "conjugation
    c = {}
    return c;

def conjugatePresent(stem, injection, gradation=False):
    pass
