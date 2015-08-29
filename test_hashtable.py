import impl_hashtable
import ref_hashtable

HT = impl_hashtable

class TestHashtable(object):
    def test_create(self):
        """Create outputs that can store state."""
        assert HT.create() is not None

    def test_put_and_get(self):
        """Basic putting and getting works."""
        ht = HT.create()
        HT.put(ht, "foo", "bar")
        assert HT.get(ht, "foo") == "bar"

    def test_put_overwrite(self):
        """The latest put is visible."""
        ht = HT.create()
        HT.put(ht, 1, 2)
        assert HT.get(ht, 1) == 2
        HT.put(ht, 1, 3)
        assert HT.get(ht, 1) == 3

    def test_put_and_get_tuple(self):
        """Tuples (a hashable type) can be used as keys."""
        ht = HT.create()
        HT.put(ht, (1, 2), 3)
        print HT.get(ht, (1, 2))
        assert HT.get(ht, (1, 2)) == 3

    def test_none_key(self):
        """None can be used as a key."""
        ht = HT.create()
        HT.put(ht, None, 4)
        assert HT.get(ht, None) == 4

    def test_put_multiple(self):
        """The table is not just a variable."""
        ht = HT.create()
        HT.put(ht, 2, 44)
        HT.put(ht, 3, 55)
        assert HT.get(ht, 2) == 44
        assert HT.get(ht, 3) == 55

    def test_remove(self):
        """Remove affects future gets."""
        ht = HT.create()
        HT.put(ht, 1, 2)
        assert HT.get(ht, 1) == 2
        HT.remove(ht, 1)
        assert HT.get(ht, 1) is None

    def test_remove_noexist(self):
        """Remove works on non-existing mappings."""
        ht = HT.create()
        HT.remove(ht, 1)
        assert HT.get(ht, 1) is None
        HT.put(ht, 1, 2)
        HT.remove(ht, 1)
        assert HT.get(ht, 1) is None

    def test_swap(self):
        """Swap returns the previous value and changes the future."""
        ht = HT.create()
        HT.put(ht, 'a', 5)
        assert HT.swap(ht, 'a', 6) == 5
        assert HT.swap(ht, 'a', 7) == 6
        assert HT.swap(ht, 'a', 8) == 7
        assert HT.get(ht, 'a') == 8
