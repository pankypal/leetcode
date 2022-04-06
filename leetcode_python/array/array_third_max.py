import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_1 = -sys.maxsize - 1
        max_2 = -sys.maxsize - 1
        max_3 = -sys.maxsize - 1

        for i in range(0,size):
            if nums[i] == max_1 or nums[i] == max_2 or nums[i] == max_3:
                continue

            if nums[i] > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = nums[i]
            elif nums[i] > max_2:
                max_3 = max_2
                max_2 = nums[i]
            elif nums[i] > max_3:
                max_3 = nums[i]

        return max_3 if max_3 != -sys.maxsize -1 else max_1


solution = Solution()
print(solution.thirdMax([2,2,3,1]))