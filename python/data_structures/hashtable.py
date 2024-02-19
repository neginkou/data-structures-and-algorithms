from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Hashtable class with set, get, has, key, and hash method
    """

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        index = 0
        prime_number = 599
        for char in key:
            index += ord(char)
        index *= prime_number
        index = index % self.size

        return index

    def set(self, key, value):
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self._buckets[index] = bucket

        current_bucket = bucket.head

        while current_bucket:
            candidate = current_bucket.value
            if candidate[0] == key:
                candidate[1] = value
                return candidate[1]


        kv_pair = [key, value]
        bucket.insert(kv_pair)
        return kv_pair[1]

    def get(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]

        if bucket is None:
            return None

        current_bucket = bucket.head

        while current_bucket:
            if current_bucket.value[0] == key:
                return current_bucket.value[1]

            current_bucket = current_bucket.next

        return None

    def has(self, key):
        for bucket in self._buckets:
            if bucket:
                current_bucket = bucket.head
                while current_bucket:
                    if current_bucket.value[0] == key:
                        return True

                    current_bucket = current_bucket.next

        return False

    def keys(self):
        keys_list = []

        for bucket in self._buckets:
            if bucket:
                current_bucket = bucket.head
                while current_bucket:
                    keys_list.append(current_bucket.value[0])
                    current_bucket = current_bucket.next

        return keys_list
