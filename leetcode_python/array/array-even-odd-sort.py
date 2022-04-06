from turtle import st


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        size = len(nums)
        end = size - 1

        while start < end:
            if nums[start] % 2 == 0:
                start += 1
            else:
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                end -= 1

        return nums


solution = Solution()
print(solution.sortArrayByParity([4, 6, 1,3,7]))