# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        res = []

        if not root:
            return res

        q.append(root)

        temp = []
        while q:
            next = []
            for node in q:
                temp.append(node.val)

                if node.left:
                    next.append(node.left)

                if node.right:
                    next.append(node.right)

            res.append(temp)
            q = next
            temp = []

        return res


        

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.levelOrder(root))