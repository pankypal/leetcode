class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.data = [None] * k
        self.head = self.tail = self.size = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.data[self.tail] = value
        self.tail = (self.tail + 1) % len(self.data)
        self.size += 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        

        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        return True
            
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[self.head]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[self.tail-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == len(self.data)

obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.Rear())