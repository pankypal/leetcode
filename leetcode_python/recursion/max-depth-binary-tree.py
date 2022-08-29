# Definition for a binary tree node.

from sys import maxunicode


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

        
solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right  = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(56)

print(solution.maxDepth(root))