# 199. Binary Tree Right Side View


# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        ans = []

        if not root:
            return ans

        curr = deque()
        curr.append(root)

        while curr:
            item = curr[0]
            ans.append(item.val)
            # temp = deque()

            length = len(curr)
            for _ in range(length):
                el = curr.popleft()
                if el.right:
                    # temp.append(el.right)
                    curr.append(el.right)
                if el.left:
                    # temp.append(el.left)
                    curr.append(el.left)

            # curr = temp

        return ans



root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
sol = Solution()
print(sol.rightSideView(root))