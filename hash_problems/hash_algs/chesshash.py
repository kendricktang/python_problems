def chess_hash(board, hashsize=24593):
    """Hashes a chess board, where a chessboard is represented by
    an array of length 64 containing 4-bit values.

    Given a valid move, it is possible to just xor the current hashval
    with the appropriate _chess_hash calls as opposed to rehashing the
    entire board."""
    hashval = 0
    for ind in xrange(64):
        hashval ^= _chess_hash(ind, board[ind], hashsize)
    return hashval


def _chess_hash(location, val, hashsize):
    """Returns a hash value dependent on the location of the piece and what
    is occupying it."""
    hashprime = 1543
    return (location * hashprime + val) % hashsize
