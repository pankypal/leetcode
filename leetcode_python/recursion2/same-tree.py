from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeIter(self, p, q):

        dq = deque([(p, q)])

        while dq:
            node1, node2 = dq.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            dq.append((node1.left, node2.left))
            dq.append((node1.right, node2.right))

        
        return True

            


        
        

solution = Solution()
root1 = TreeNode(1)
root2 = TreeNode(1, right=TreeNode(2))
print(solution.isSameTree(root1, root2))
print(solution.isSameTreeIter(root1, root2))