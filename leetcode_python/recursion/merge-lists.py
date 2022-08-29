# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        head = self
        ret = "["
        while head:
            ret += str(head.val) + ","
            head = head.next

        return ret + "]"
        

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ret = res = ListNode()
        while list1 and list2:
            temp = None
            if list1.val < list2.val:
                temp = list1.val
                list1 = list1.next
            else:
                temp = list2.val
                list2 = list2.next

            res.next = ListNode(temp)
            res = res.next
        
        while list1:
            res.next = ListNode(list1.val)
            list1 = list1.next
            res = res.next


        while list2:
            res.next = ListNode(list2.val)
            list2 = list2.next
            res = res.next

        return ret.next

solution = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(4)

print(solution.mergeTwoLists(list1, list2))