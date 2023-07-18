"""
Vampire Numbers
Our loose definition of Vampire Numbers can be described as follows:

6 * 21 = 126
# 6 and 21 would be valid 'fangs' for a vampire number as the
# digits 6, 1, and 2 are present in both the product and multiplicands

10 * 11 = 110
# 110 is not a vampire number since there are three 1's in the
# multiplicands, but only two 1's in the product
"""

#Solution
def vampire_test(x, y):
    z = x * y
    num_z= list(str(z))
    num_o = list(str(x))+list(str(y))
    if sorted(num_z)==sorted(num_o) and len(num_o)==len(num_z):
         return True
    else:
         return False