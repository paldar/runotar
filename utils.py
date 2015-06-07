#contains random utility functions

import random, string

#credit:
#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def generateRandomString(length):
    return ''.join(random.SystemRandom().choice(string.digits + string.ascii_letters) for _ in range(length))

