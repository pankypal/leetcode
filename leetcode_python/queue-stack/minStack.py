from collections import deque

class MinStack(object):
    def __init__(self):
        self.mainStack = deque()
        self.auxStack = deque()

    def push(self, val):
        if not self.mainStack:
            lastVal = val
        else:
            lastVal = self.auxStack[-1]
        self.mainStack.append(val)
        if lastVal >= val or not self.auxStack:
            self.auxStack.append(val)

    def pop(self):
        if self.auxStack[-1] == self.mainStack[-1]:
            self.auxStack.pop()

        return self.mainStack.pop()

    def top(self):
        return self.mainStack[-1]

    def getMin(self):
        return self.auxStack[-1]


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin())
print(minStack.top())
minStack.pop()
print(minStack.getMin())