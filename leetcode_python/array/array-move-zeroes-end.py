from asyncore import read


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        read_index = 0
        count_zeros = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[read_index], nums[i] = nums[i], nums[read_index]
                read_index += 1



solution = Solution()
nums =  [0, 2, 0, 5]
solution.moveZeroes(nums)
print(nums)