from stringhash import string_hash


def pairusers(userset):
    """Walks through a set of users. If the current user is paired with
    a previous user, then they are matched and yielded."""
    hashset = {}
    for user in userset:
        hashval = string_hash(user.attributes)
        if hashval in hashset:
            otheruser = hashset.pop(hashval)
            yield (user, otheruser)
        else:
            hashset[hashval] = user


class MyUser(object):
    """A user object."""
    def __init__(self, integerkey, attributes):
        """integerkey is a 32-bit integer. Attributes is a set of strings."""
        self.integerkey = integerkey
        attributes.sort()
        self.attributes = "".join(attributes)
