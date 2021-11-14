"""
>>> main()  # doctest: +NORMALIZE_WHITESPACE
DEMO: bisect_right
haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30
31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31
30 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |30
29 @ 13      |  |  |  |  |  |  |  |  |  |  |  |  |29
23 @ 11      |  |  |  |  |  |  |  |  |  |  |23
22 @  9      |  |  |  |  |  |  |  |  |22
10 @  5      |  |  |  |  |10
 8 @  5      |  |  |  |  |8
 5 @  3      |  |  |5
 2 @  1      |2
 1 @  1      |1
 0 @  0    0
"""
#bisect(haystack, needle) does a binary search for needle in haystack — which
#must be a sorted sequence — to locate the position where needle can be inserted while
#maintaining haystack in ascending order. In other words, all items appearing up to that
#position are less or equal to needle. You could use the result of bisect(haystack,
#needle) as the index argument to haystack.insert(index, needle), but using in
#sort does both steps, and is faster.

#Use the chosen bisect function to get the insertion point.
#Build a pattern of vertical bars proportional to the offset.
#Print formatted row showing needle and insertion point.
#Choose the bisect function to use according to the last command line argument.
#Print header with name of function selected.

#sys
#This module provides access to some variables used or maintained by the interpreter and to functions that
#interact strongly with the interpreter. It is always available.

#First, a pair of optional arguments lo and hi allow narrowing the region in the sequence
#to be searched when inserting. lo defaults to 0 and hi to the len() of the sequence.
#Second, bisect is actually an alias for bisect_right, and there is a sister function called
#bisect_left. Their difference is apparent only when the needle compares equal to an
#item in the list: bisect_right returns an insertion point after the existing item, and
#bisect_left returns the position of the existing item, so insertion would occur before
#it. With simple types like int this makes no difference, but if the sequence contains
#objects that are distinct yet compare equal, then it may be relevant. For example, 1 and
#1.0 are distinct, but 1 == 1.0 is True.

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]

#Haystack provides modular search for Django. It features a unified, familiar API that allows you to plug in
#different search backends (such as Solr, Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code.

NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

#Needle is a tool for testing visuals with Selenium and nose.

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'



def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

#These functions are not only used for searching, but also for inserting items in sorted
#sequences, as the following section shows


def main():
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


if __name__ == '__main__':
    main()
