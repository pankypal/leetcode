from math import remainder


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output = []
        self._permute(nums, [], output)
        return output

    def _permute(self, nums, prefix, output):
        if len(nums) == 0:
            output.append(prefix)
            return

        for n in range(len(nums)):
            curr = nums[n]
            remainder = nums[:n] + nums[n+1:]
            self._permute(remainder, prefix + [curr], output)


        

solution = Solution()
print(solution.permute([1,2,3]))