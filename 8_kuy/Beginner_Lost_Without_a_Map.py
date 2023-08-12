"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""

#Solution
def maps(a):
    x = []
    for i in a:
        x.append(2 * i)
    return x