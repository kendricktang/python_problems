from collections import defaultdict
from stringhash import string_hash
from string import whitespace


def findanagrams(stringdict):
    """Generates sets words which are anagrams of each other in a dictionary."""
    hashset = defaultdict(list)
    for string in stringdict:
        hashset[string_hash(''.join(sorted(string)))].append(string)

    for hashval in hashset:
        if len(hashset[hashval]) > 1:
            yield hashset[hashval]


def islettersubsetofmagazine(letter, magazine):
    """Checks to see if letter is a subset of magazine."""
    letterset = defaultdict(int)

    # Put the letter into the letterset.
    for c in letter:
        if c not in whitespace:
            letterset[c] += 1

    # Remove the letter from the letterset.
    for c in magazine:
        if c not in whitespace:
            letterset[c] -= 1
            if not letterset[c]:
                letterset.remove(c)
        if not letterset:
            # All the characters from the letter have a source from the magazine
            return True
    # Not even the entire magazine has enough characters for form the letter.
    return False
