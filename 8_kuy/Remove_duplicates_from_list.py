"""Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same."""

def distinct(seq):
    seq = list(dict.fromkeys(seq))
    return seq