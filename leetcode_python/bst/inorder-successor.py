class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorder_successor(self, root, p):
        if not root:
            return None

        succ = None

        if p.right:
            return self.findMin(p)

        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > p.val:
                succ = root
                root = root.left
            else:
                break

        return succ

    def findMin(root):
        while root.left:
            root = root.left

        return root    

        

root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.right = TreeNode(12)
root.left.left = TreeNode(8)
root.right.left = TreeNode(16)
root.right.right = TreeNode(25)

solution = Solution()
succ = solution.inorder_successor(root, root.left.right)
print(succ.val)