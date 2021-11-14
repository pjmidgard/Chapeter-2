# Chapeter-2
Chapeter 2
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


#Haystack provides modular search for Django. It features a unified, familiar API that allows you to plug in
#different search backends (such as Solr, Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code.


#An interesting application of bisect is to perform table lookups by numeric values, for
#example to convert test scores to letter grades,

#which also lists
#functions to use bisect as a faster replacement for the index method when searching
#through long ordered sequences of numbers.
#These functions are not only used for searching, but also for inserting items in sorted
#sequences, as the following section shows.



#Needle is a tool for testing visuals with Selenium and nose.
