# 334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return false

        first = nums[0]
        second = float("inf")

        for num in nums:
            if num > second:
                return True
            
            if num > first and num < second:
                second = num

            if num <= first:
                first = num
            

        return False

        

sol = Solution()
print(sol.increasingTriplet([1,2,3,4,5]))
print(sol.increasingTriplet([2,4,-2,-3]))