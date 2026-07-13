# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return
        
        nonzero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                nonzero = i + 1
                while nonzero < len(nums) and nums[nonzero] == 0:
                    nonzero += 1

                if nonzero < len(nums):
                    nums[i], nums[nonzero] = nums[nonzero], nums[i]

        return nums
        

sol = Solution()
print(sol.moveZeroes([0]))