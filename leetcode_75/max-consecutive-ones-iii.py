# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k >= nums.count(0):
            return len(nums)
        
        left = 0
        zeroes = 0
        max_len = 0

        for right in range(len(nums)):
            zeroes += nums[right] == 0

            while zeroes > k:
                zeroes -= nums[left] == 0
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        

sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))