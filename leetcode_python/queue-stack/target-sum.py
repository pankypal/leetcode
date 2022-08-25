class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.memo = {}

        return self.findWays(nums, 0, 0, target)


    def findWays(self, nums, index, currSum, target):
        if (index, currSum) in self.memo:
            return self.memo[(index, currSum)]
        
        if index == len(nums):
            if target == currSum:
                return 1
            else:
                return 0

        pos = self.findWays(nums, index+1, currSum+nums[index], target)
        neg = self.findWays(nums, index+1, currSum-nums[index], target)

        self.memo[(index, currSum)] = pos + neg
        return pos + neg

    def findTargetSumWaysDP(self, nums, target):
        total = sum(nums)
        dp = [0] * (2*total + 1)

        if target > abs(total):
            return 0

        dp[nums[0]+total] = 1
        dp[-nums[0]+total] = 1

        for i in range(1, len(nums)):
            nextdp = [0] * (2*total+1)
            for j in range(-total, total+1):
                if dp[j+total] > 0:
                    nextdp[j+nums[i]+total] += dp[j+total]
                    nextdp[j-nums[i]+total] += dp[j+total]
            dp = nextdp

        return dp[target+total]
        

solution = Solution()
print(solution.findTargetSumWays([1,1,1,1,1], 3))
print(solution.findTargetSumWaysDP([1,1,1,1,1], 3))