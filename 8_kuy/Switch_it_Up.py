"""
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".
"""
#Solution
def switch_it_up(n):
    if n == 1: return "One"
    elif n == 2: return "Two"
    elif n == 3: return "Three"
    elif n == 4: return "Four"
    elif n == 5: return "Five"
    elif n == 6: return "Six"
    elif n == 7: return "Seven"
    elif n == 8: return "Eight"
    elif n == 9: return "Nine"
    else: return "Zero"