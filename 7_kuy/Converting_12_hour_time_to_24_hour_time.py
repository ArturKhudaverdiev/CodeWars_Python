"""
Converting a normal (12-hour) time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function named "to24hourtime", and you will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.
"""
#Solution
from datetime import *
def to24hourtime(hour, minute, period):
    t = f'{hour}:{minute} {period}'
    return datetime.strptime(t, '%I:%M %p').strftime('%H%M')