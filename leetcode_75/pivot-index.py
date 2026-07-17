# 724. Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to 
# the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are 
# no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return -1
        
        total = sum(nums)
        
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            
            left += nums[i]

        return -1



sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))
print(sol.pivotIndex([1,2,3]))
print(sol.pivotIndex([2,1,-1]))