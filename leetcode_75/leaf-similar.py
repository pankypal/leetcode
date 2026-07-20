# 872. Leaf-Similar Trees

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        list1 = []
        list2 = []

        self._leafSimilar(root1, list1)
        self._leafSimilar(root2, list2)

        return list1 == list2
    
    def _leafSimilar(self, root, path):
        if not root:
            return
        
        if root.left is None and root.right is None:
            path.append(root.val)
            return
        
        self._leafSimilar(root.left, path)
        self._leafSimilar(root.right, path)
        

root1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))

sol = Solution()
print(sol.leafSimilar(root1, root2))