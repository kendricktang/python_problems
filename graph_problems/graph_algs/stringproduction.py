from collections import deque
from string import ascii_lowercase as letters


def findproductionseq(string_dict, s, t):
    """Given a list of strings (string_dict), the shorted production sequence
    from s to t is searched for via BFS. Note: string_dict is not modified."""
    if not len(s) == len(t):
        return None
    if s not in string_dict or t not in string_dict:
        return None

    queue = deque()
    queue.append([s])
    visited = set()
    while queue:
        path = queue.popleft()
        word = path[-1]
        for nextword in _findnextwords(string_dict, word) - visited:
            visited.add(nextword)
            if nextword == t:
                return path + [nextword]
            else:
                queue.append(path + [nextword])
    return -1


def _findnextwords(string_dict, word):
    """Finds words that are similar to word in the string_dict and
    returns them as a set."""
    newwords = set()
    for ind in xrange(len(word)):
        for letter in letters:
            newword = word[:ind] + letter + word[ind+1:]
            if newword in string_dict:
                newwords.add(newword)
    return newwords


if __name__ == "__main__":
    string_dict = [
        'cat',
        'bat',
        'bbt',
        'bbm',
        'bam',
        'bum',
        'but',
        'cut'
    ]
    print findproductionseq(string_dict, 'cut', 'bbm')
