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
                nums[read_index] = nums[i]
                read_index += 1
            else:
                count_zeros += 1

        end = len(nums) - 1
        while count_zeros > 0:
            nums[end] = 0
            end -= 1
            count_zeros -= 1


solution = Solution()
nums =  [0, 0, 0, 0]
solution.moveZeroes(nums)
print(nums)