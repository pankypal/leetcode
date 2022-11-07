# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        return self._sortedArrayToBst(nums, 0, len(nums)-1)

    def _sortedArrayToBst(self, nums, start, end):
        if start > end:
            return None

        mid = (start+end) // 2
        
        node = TreeNode(nums[mid])
        node.left = self._sortedArrayToBst(nums, start, mid-1)
        node.right = self._sortedArrayToBst(nums, mid+1, end)

        return node


solution = Solution()
solution.sortedArrayToBST([-10,-3,0,5,9])