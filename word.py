#hamming distance from wikipedia
#url: https://en.wikipedia.org/wiki/Hamming_distance
def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


class Word:
    def __init__(self, title, wordType):
        self.title = title;
        self.wordType = wordType;
    def __str__(self):
        return self.title + " " + self.wordType;
