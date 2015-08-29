"""
Challenge 1 : Hash Table
Implementation of a hash table.

A hash table stores a mapping from keys to values.
"""

def create():
    """Create a new hash table."""

def put(ht, key, value):
    """Put a mapping into the hash table.

    Adds a mapping to the hash table.
    If a mapping already exists from this key, replace the existing mapping.

    Args:
        ht: The hashtable object to modify.
        key: The (hashable) key from which to map.
        value: The value to map to.
    """
    raise NotImplementedError()

def get(ht, key):
    """Get the value assosciated with the key from the hash table.

    Args:
        ht: The hashtable object to modify.
        key: The (hashable) key from which to map.
        value: The value to map to.

    Returns:
        The value assosciated with the key.
        Or None if no such mapping exists.
    """
    raise NotImplementedError()

def remove(ht, key):
    """Removes the mapping from this key.

    Args:
        ht: The hashtable object to modify.
        key: The (hashable) key to dissociate.
    """
    raise NotImplementedError()

def swap(ht, key, value):
    """Swap a new value out for the one mapped to by key.

    Swap in a new value and return the old one.
    If a mapping already exists from this key, replace the existing mapping.
    If a mapping does not already exist, add one.

    Args:
        ht: The hashtable object to modify.
        key: The (hashable) key from which to map.
        value: The value to map to.

    Returns:
        The value previously assosciated with key.
        Or None if no such mapping existed.
    """
    raise NotImplementedError()
