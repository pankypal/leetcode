class MyHashSet(object):

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket, idx = self._index(key)

        if idx == -1:
            bucket.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket, idx = self._index(key)

        if idx != -1:
            bucket.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        _, idx = self._index(key)

        return idx != -1

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        _hash = key % self.size
        bucket = self.buckets[_hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        
        return bucket, -1
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))
