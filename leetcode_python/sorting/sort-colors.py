class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1

        curr = 0
        while curr <= end:
            if nums[curr] == 0:
                nums[curr], nums[start] = nums[start], nums[curr]
                start += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[end], nums[curr] = nums[curr], nums[end]
                end -= 1

        return nums



solution = Solution()
solution.sortColors([2,0,1,1,1])