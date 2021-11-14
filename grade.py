"""
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']
"""

#An interesting application of bisect is to perform table lookups by numeric values, for
#example to convert test scores to letter grades,

#which also lists
#functions to use bisect as a faster replacement for the index method when searching
#through long ordered sequences of numbers.
#These functions are not only used for searching, but also for inserting items in sorted
#sequences, as the following section shows.

import bisect


def grade(score, breakpoints=(60, 70, 80, 90), grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

grades = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(grades)
