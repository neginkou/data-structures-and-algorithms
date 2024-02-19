# Challenge Title

# Hashtable


## Approach & Efficiency

The Hashtable class uses an array of linked lists to handle collisions. The _hash method calculates the index for a key, and the set method adds or updates key-value pairs in the appropriate bucket. The get method retrieves values, the has method checks for key existence, and the keys method returns a list of all keys.

Big O Complexity:

Space: O(n), where n is the number of key-value pairs.
Time:
_hash: O(k), where k is the key length.
set/get: Average O(1), worst O(n) due to possible collisions.
has/keys: O(n), as they may need to iterate through all buckets and lists.

## Solution

[Code Solution](/python/data_structures/hashtable.py)
