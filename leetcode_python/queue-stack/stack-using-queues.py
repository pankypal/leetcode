from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.q:
            raise "Empty Stack"

        return self.q.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.q:
            raise "Empty Stack"

        return self.q[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())