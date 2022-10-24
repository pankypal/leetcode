from json.encoder import INFINITY


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return self._isValidBST(root, float("-inf"), float("inf"))

    def _isValidBST(self, node, lowBound, upperBound):
        if not node:
            return True

        return (
            node.val > lowBound 
            and node.val < upperBound 
            and self._isValidBST(node.left, lowBound, node.val) 
            and self._isValidBST(node.right, node.val, upperBound))



solution = Solution()
root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(5)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(6)
print(solution.isValidBST(root))