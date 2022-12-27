# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        result = ListNode()
        curr = head

        while curr:
            list = result
            while list.next and list.next.val <= curr.val:
                list = list.next


            next = curr.next
            curr.next = list.next
            list.next = curr

            curr = next

        return result.next


solution = Solution()
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
solution.insertionSortList(head)