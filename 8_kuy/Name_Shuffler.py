"""
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"
"""
#Solution
def name_shuffler(str):
    return ' '.join(reversed(str.split()))