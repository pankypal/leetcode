# 1372. Longest ZigZag Path in a Binary Tree 

# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        return max(self._longestZigZag(root.left, False, 0), self._longestZigZag(root.right, True, 0))

    def _longestZigZag(self, root, isRight, length):
        if not root:
            return length

        if isRight:
            return max(self._longestZigZag(root.left, False, length+1), self._longestZigZag(root.right, True, 0))
        else:
            return max(self._longestZigZag(root.right, True, length+1), self._longestZigZag(root.left, False, 0))
        

root = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1)))))
sol = Solution()
print(sol.longestZigZag(root))