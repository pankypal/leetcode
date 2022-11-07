# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced, _ = self._isBalanced(root)
        return balanced

    def _isBalanced(self, root):
        if not root:
            return (True, 0)

        lbalanced, lh = self._isBalanced(root.left)
        rbalanced, rh = self._isBalanced(root.right)

        balanced = lbalanced and rbalanced and abs(lh - rh) <= 1
        return (balanced, max(lh, rh)+1)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

solution = Solution()
print(solution.isBalanced(root))