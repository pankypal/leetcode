# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head
        
        prev = None
        curr = head

        while curr:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next

        return prev
        


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

sol = Solution()
sol.reverseList(head)