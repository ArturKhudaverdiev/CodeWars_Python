"""
DESCRIPTION:
Make a function that returns the value multiplied by 50 and increased by 6.
If the value entered is a string it should return "Error".
"""

#Solution

def problem(a):
    if type(a) == str:
        return "Error"
    else:
        return (a * 50) + 6