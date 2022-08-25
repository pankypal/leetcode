# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        if not root:
            return res

        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]
            stack.pop()
            res.append(curr.val)

            curr = curr.right

        return res
        

solution = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(solution.inorderTraversal(root))