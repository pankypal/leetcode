class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        curr = head
        prev = None
        while curr and curr.next:
            if curr == head:
                head = curr.next

            if prev:
                prev.next = curr.next

            temp = curr.next.next
            curr.next.next = curr
            curr.next = temp


            prev = curr
            curr = temp

        return head


solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
#head.next.next.next = ListNode(4)
head = solution.swapPairs(head)
print(head)