#definition of kotus types, and their declension/conjugation.
import kotus.verb;


#returns a dictionary, similar to the list on wiktionary
def conjugate(stem, kotusType):
    return getattr(kotus.verb, "conjugate"+kotusType)(stem);