# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        maxSum, _ = self._pairSum(head, head, float("-inf"))
        return maxSum
    
    def _pairSum(self, head, pair, maxSum):
        if not head:
            return float("-inf"), pair
        
        s, p =  self._pairSum(head.next, pair, maxSum)
        return (max(s, head.val + p.val), p.next)
    
    def pairSum1(self, head):
        def reverse(head):
            dummy = ListNode()
            curr = head
            while curr:
                next = curr.next
                curr.next = dummy.next
                dummy.next = curr
                curr = next
            return dummy.next

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        pa = head
        q = slow.next
        slow.next = None
        pb = reverse(q)
        ans = 0
        
        while pa and pb:
            ans = max(ans, pa.val + pb.val)
            pa = pa.next
            pb = pb.next
        return ans
        

head = ListNode(5,ListNode(4,ListNode(2,ListNode(1))))
sol = Solution()
print(sol.pairSum(head))