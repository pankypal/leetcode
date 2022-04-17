class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        left = 0
        right = 1
        sum = 0

        while right < len(nums):
            sum += min(nums[left], nums[right])
            left += 2
            right += 2

        return sum

solution = Solution()
print(solution.arrayPairSum([6,2,6,5,1,2]))