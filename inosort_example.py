"""
>>> random.seed(1729)
>>> main()
10 -> [10]
 0 -> [0, 10]
 6 -> [0, 6, 10]
 8 -> [0, 6, 8, 10]
 7 -> [0, 6, 7, 8, 10]
 2 -> [0, 2, 6, 7, 8, 10]
10 -> [0, 2, 6, 7, 8, 10, 10]
"""
#Like bisect, insort takes optional lo, hi arguments to limit the search to a subsequence. There is also an insort_left variation that uses bisect_left to find inser‐
#tion points.
#Much of what we have seen so far in this chapter applies to sequences in general, not
#just lists or tuples. Python programmers sometimes overuse the list type because it is
#so handy — I know I’ve done it. If you are handling lists of numbers, arrays are the way
#to go. The remainder of the chapter is devoted to them.

import bisect
import random

SIZE = 7

random.seed(1729)


def main():
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)


if __name__ == '__main__':
    main()
