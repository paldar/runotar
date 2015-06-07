#contains definitions for language specific variables
#should apply to whole language.

vowels = ['a','o','i','e', 'u', 'ä', 'ö', 'y']

vowelHarmonyDict = {
    'a':'ä',
    'o':'ö',
    'u':'y',
    'ä':'a',
    'ö':'o',
    'y':'u',
}
#hard coded word pattern: regex
# (vowel)*{0,1,2}(consonant)*{0,1,2}
wordPattern = ""

def isWordLike(word):
    pass
