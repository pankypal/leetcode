# 328. Odd Even Linked List

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_start = even

        curr = even.next if even else None

        while curr:
            odd.next = curr
            odd = odd.next

            even.next = curr.next
            even = even.next
            
            curr = curr.next.next if curr.next else curr.next

        if even_start:
            odd.next = even_start

        return head
        

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
sol.oddEvenList(head)