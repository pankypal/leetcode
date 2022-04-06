from numpy import cumsum


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_so_far = 0
        current_max = 0
        for num in nums:
            if num == 0:
                current_max = 0
            else:
                current_max += 1
                max_so_far = max(max_so_far, current_max)
        
        return max_so_far

solution = Solution()
print(solution.findMaxConsecutiveOnes([0,1,0,1,1,1]))