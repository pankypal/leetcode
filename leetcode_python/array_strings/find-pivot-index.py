import enum


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        rightSum = sum(nums)

        for i, num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                return i
            
            leftSum += num

        return -1
             

solution = Solution()
print(solution.pivotIndex([-1,-1,-1,1,1,1]))