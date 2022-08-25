class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if not self.stack1:
            self.front = x

        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            raise "Empty stack"
            
        if not self.stack2:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)

        return self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            raise "Empty stack"

        if self.stack2:
            return self.stack2[-1]
        return self.front
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack1) + len(self.stack2) == 0:
            return True

        return False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())