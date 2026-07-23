# 1161. Maximum Level Sum of a Binary Tree

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Definition for a binary tree node.

from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        maxSum = float("-inf")
        maxLevel = 0
        ans = 0
        curr = deque([root])

        while curr:
            length = len(curr)

            val = 0
            for _ in range(length):
                el = curr.popleft()
                val += el.val

                if el.left:
                    curr.append(el.left)
                if el.right:
                    curr.append(el.right)

            ans += 1
            if val > maxSum:
                maxLevel = ans
                maxSum = val

        return maxLevel


root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
sol = Solution()
print(sol.maxLevelSum(TreeNode(1)))