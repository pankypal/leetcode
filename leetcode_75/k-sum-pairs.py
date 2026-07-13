# 1679. Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k. 
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums:
            return 0
        
        nums = sorted(nums)

        i = 0
        j = len(nums) - 1
        count = 0

        while i < j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1

        return count        


sol = Solution()
print(sol.maxOperations([3,1,3,4,3], 6))