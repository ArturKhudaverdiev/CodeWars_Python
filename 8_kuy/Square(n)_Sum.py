"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.
"""

#Solution
def square_sum(numbers):
    return sum([i * i for i in numbers])