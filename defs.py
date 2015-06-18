#contains definitions for language specific variables
#should apply to whole language.
import re,string

vowels = ['a','o','i','e', 'u', 'ä', 'ö', 'y']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z','ž','š']

vowelHarmonyDict = {
    'a':'ä',
    'o':'ö',
    'u':'y',
    'ä':'a',
    'ö':'o',
    'y':'u',
}

wordTypes = [
    'Verb',
    'Noun',
    'Adverb',
    'Adjective',
    'Interjection',
    'Pronoun',
    'Postposition',
    'Preposition',
    'Numeral',
    'Suffix',
    'Abbreviation'
]
#hard coded word pattern: regex
wordPattern = "(["+"".join(vowels)+"]{1,2}|(["+"".join(consonants)+"]["+"".join(vowels)+"]))((["+"".join(vowels)+"]|["+"".join(consonants)+"]){1,2})*"

def isWordLike(word):
    word = word.lower()
    rex = re.search(wordPattern, word);
    return (rex) and (rex.group(0) == word)
