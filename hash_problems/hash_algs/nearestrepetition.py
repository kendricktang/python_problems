from stringhash import string_hash


def findnearestrepetition(stringarray):
    """Returns the smallest distance between two equal entries in the array.
    If the set is unique, returns -1."""
    hashset = {}
    smallestdist = len(stringarray)
    for index in xrange(smallestdist):
        string = stringarray[index]
        hashval = string_hash(string)
        if hashval not in hashset:
            hashset[hashval] = index
        else:
            lastindex = hashset[hashval]
            smallestdist = min(smallestdist, index - lastindex)

    if smallestdist == len(stringarray):
        return -1
    return smallestdist


if __name__ == "__main__":
    sarray = [
        "All", "work", "and", "no", "play", "makes", "for", "no", "work", "no",
        "run", "and", "no", "results"]
    print "Should be 2:", findnearestrepetition(sarray)
