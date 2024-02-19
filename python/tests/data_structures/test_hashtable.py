import unittest
from data_structures.linked_list import LinkedList
from data_structures.hashtable import Hashtable

class TestHashtable(unittest.TestCase):

    def setUp(self):
        self.hashtable = Hashtable()

    def test_hash(self):
        # Test that the hash function generates consistent indices
        self.assertEqual(self.hashtable._hash("key1"), self.hashtable._hash("key1"))

    def test_set_and_get(self):
        # Test setting and getting key-value pairs
        self.hashtable.set("key1", "value1")
        self.assertEqual(self.hashtable.get("key1"), "value1")

    def test_update_value(self):
        # Test updating the value for an existing key
        self.hashtable.set("key1", "value1")
        self.hashtable.set("key1", "value2")
        self.assertEqual(self.hashtable.get("key1"), "value2")

    def test_get_nonexistent_key(self):
        # Test getting a value for a nonexistent key
        self.assertIsNone(self.hashtable.get("nonexistent"))

    def test_has_key(self):
        # Test checking if a key exists in the hashtable
        self.hashtable.set("key1", "value1")
        self.assertTrue(self.hashtable.has("key1"))
        self.assertFalse(self.hashtable.has("nonexistent"))

    def test_keys(self):
        # Test retrieving all keys
        self.hashtable.set("key1", "value1")
        self.hashtable.set("key2", "value2")
        self.assertListEqual(sorted(self.hashtable.keys()), ["key1", "key2"])

if __name__ == "__main__":
    unittest.main()
