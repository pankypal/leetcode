# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 
# p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        return self.lca(root, p, q)

    def lca(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        left_lca = self.lca(root.left, p, q)
        right_lca = self.lca(root.right, p, q)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca else right_lca



root = TreeNode(3)
p = root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
q = root.left.right.right = TreeNode(4)

sol = Solution()
ans = sol.lowestCommonAncestor(root, p, q)
print(ans.val)