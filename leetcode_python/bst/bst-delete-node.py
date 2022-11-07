# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if not root:
            return root

        found = False
        pred = None

        curr = root
        while curr:
            if curr.val == key:
                found = True
                break
            elif curr.val < key:
                pred = curr
                curr = curr.right
            else:
                pred = curr
                curr = curr.left
        
        if not found:
            return root

        # case 1: both children
        if curr.left and curr.right:
            # find successor
            succ = curr.right
            pred_succ = curr
            while succ.left:
                pred_succ = succ
                succ = succ.left

            curr.val, succ.val = succ.val, curr.val
            curr = succ
            pred = pred_succ

        # case 2: no child
        child = None
        
        # case 3: one child
        if curr.left or curr.right:
            child = curr.left if curr.left else curr.right

        if pred == None:
            root = child
        else:
            if pred.left == curr:
                pred.left = child
            else:
                pred.right = child

        return root

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

solution = Solution()
solution.deleteNode(root, 1)
