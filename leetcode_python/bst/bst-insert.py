# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        pred = None
        curr = root
        while curr:
            if curr.val > val:
                pred = curr
                curr = curr.left
            else:
                pred = curr
                curr = curr.right

        if not pred:
            return TreeNode(val)
        else:
            if pred.val > val:
                pred.left = TreeNode(val)
            else:
                pred.right = TreeNode(val)

        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
solution.insertIntoBST(None, 5)