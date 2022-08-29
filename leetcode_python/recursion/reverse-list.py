class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseListIter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev = None
        curr = head
        next = head.next

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev
        return head

    def reverseListRec(self, head):
        if not head or not head.next:
            return head

        return self._reverse(head)

    def _reverse(self, head):
        if not head.next:
            return head

        rest = self._reverse(head.next)
        head.next.next = head
        head.next = None

        return rest

solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head = solution.reverseListIter(head)
head = solution.reverseListRec(head)
print(head)