# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        self.updateStack(root)

    def next(self):
        """
        :rtype: int
        """
        retVal = self.st.pop()
        self.updateStack(retVal.right)
        return retVal.val        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) > 0

    def updateStack(self, root):
        while root:
            self.st.append(root)
            root = root.left
        


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

obj = BSTIterator(root)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
