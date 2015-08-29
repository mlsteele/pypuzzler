# Python Puzzler

This is a set of two python challenges.
Your task is to write a implementation that solves
the challenges and passes the tests.

## Challenge 1 : Hash Table

A hashtable efficiently stores a mapping from keys to values.
Python has hashtables built-in as the `dict` type.

Your task in this challenge is to implement a dictionary
without using the `dict` type.

Write your solution in impl_hashtable.py
- create
- put
- get
- remove
- swap

## Challenge 2 : Multiset

A `set` in python is a datatype for a mathematical set.
A set is a collection of elements with no order or count.
For example the sets {a, b, c} and {c, b, a} are equivalent.
You can create sets from lists like this `set([1, 2, 3])`.
Because sets have no information about count, `set([1, 2, 3]) == set([1, 2, 2, 3])`.

Your task in this challenge is to implement a multiset.
A multiset is like a set except that it _does_ have information about count.
It knows how many times each element occurs in the set.
It still does not care what order the elements appear.

Examples:

    - `multiset([1,2,2,3]) == multiset([3,1,2,2])
    - `multiset([1,2,3]) != multiset([1,2,2,3])

Write your implementation in impl_multiset.py
Hint: You can use your hash table from challenge 1.
- create
- add
- remove
- count
- size
