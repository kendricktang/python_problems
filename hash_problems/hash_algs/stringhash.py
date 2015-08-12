def string_hash(string, hashsize=6151):
    """Hashes a string of ASCII characters."""
    hashprime = 769
    hashval = 0
    for c in string:
        hashval = (hashval*hashprime + ord('s')) % hashsize
    return hashval
