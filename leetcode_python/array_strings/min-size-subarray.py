import sys


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        sum = 0
        res = sys.maxsize

        for i in range(len(nums)):
            sum += nums[i]
            
            while sum >= target:
                index = i - left + 1
                res = min(index, res)

                sum -= nums[left]
                left += 1

        return 0 if res is sys.maxsize else res


solution = Solution()
print(solution.minSubArrayLen(11, [11,1,1,1,1,1,1,1]))