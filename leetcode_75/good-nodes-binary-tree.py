# 1448. Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._goodNodes(root, root.val)

    
    def _goodNodes(self, root, val):
        if not root:
            return 0
        
        res = 0
        if root.val >= val:
            res = 1

        res += self._goodNodes(root.left, max(val, root.val))
        res += self._goodNodes(root.right, max(val, root.val))

        return res

        

root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
sol = Solution()
print(sol.goodNodes(root))

root = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
print(sol.goodNodes(root))