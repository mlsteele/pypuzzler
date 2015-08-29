"""
Challenge 1 : Hash Table
Reference implementation of a hash table.

This just proxies to the built-in `dict` type.
For use in testing challenge implementations.
"""

def create():
    return {}

def put(ht, key, value):
    ht[key] = value

def get(ht, key):
    return ht.get(key, None)

def remove(ht, key):
    if key in ht:
        del ht[key]

def swap(ht, key, value):
    prev = ht.get(key, None)
    ht[key] = value
    return prev
