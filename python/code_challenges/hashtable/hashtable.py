from code_challenges.hashtable.linked_list_for_hash import Node, LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size
    
    def _hash(self, key):
        hash_total = 0

        for ch in key:
            hash_total += ord(ch)
        
        return (hash_total * 211) % self._size

    def add(self, key, value):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].add((key, value))
    
    def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            current = current.next
    
    def contains(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        if not bucket == None:    
            current = bucket.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        return False


