class ListNode(object):
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):

    def __init__(self):
        self.size = 997
        self.table = [ListNode() for _ in range(self.size)] 

    def hashCode(self, key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = self.hashCode(key)
        head = self.table[idx]
        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        head.next = ListNode(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        idx = self.hashCode(key)
        head = self.table[idx]
        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self.hashCode(key)
        head = self.table[idx]
        while head.next:
            if head.next.key == key:
                temp = head.next
                head.next = temp.next
                temp.next = None
                return
            head = head.next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
print(obj.get(1))
obj.remove(1)
print(obj.get(1))
