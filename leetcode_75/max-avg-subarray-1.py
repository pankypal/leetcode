# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        if k > len(nums):
            return sum(nums) / len(nums)
        
        sum = 0.0
        j = 0

        while j < k:
            sum += nums[j]
            j += 1

        i = 0
        maxSum = sum

        while i < len(nums) - k:
            sum = sum - nums[i] + nums[j]

            maxSum = max(maxSum, sum)

            i += 1
            j += 1

        return maxSum / k
        

sol = Solution()
print(sol.findMaxAverage([0,1,1,3,3], 4))
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
print(sol.findMaxAverage([0,4,0,3,2], 1))
print(sol.findMaxAverage([5], 1))