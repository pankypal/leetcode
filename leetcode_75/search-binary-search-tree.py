# 700. Search in a Binary Search Tree

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        while root:
            if root.val == val:
                return root

            if root.val < val:
                root = root.right
            else :
                root = root.left

        return root


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
sol = Solution()
ans = sol.searchBST(root, 6)
print(ans.val)
