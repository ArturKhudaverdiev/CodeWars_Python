"""
Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

Division by zero should return an empty value.
"""

#Solution 1
def remainder(a,b):
    maximum = max(a, b)
    minimum = min(a, b)
    if minimum == 0:
        return None
    return maximum % minimum

#Solution 2
def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else:
        return b % a