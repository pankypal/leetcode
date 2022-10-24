class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            root.left = root.right = root
            return root

        left = self.treeToDoublyList(root.left)
        right = self.treeToDoublyList(root.right)
        
        head = left if left else root
        tail = right.left if right else root

        if left:
            left.left.right = root
            root.left = left.left
        if right:
            root.right = right
            right.left = root

        head.left = tail
        tail.right = head
        
        return head

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(7)

solution = Solution()
ans = solution.treeToDoublyList(root)
print(ans)