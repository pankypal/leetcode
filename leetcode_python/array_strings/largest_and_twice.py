class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -1
        largestIndex = -1
        for i in range(len(nums)):
            if (nums[i] > largest):
                largest = nums[i]
                largestIndex = i
        
        for num in nums:
            if num != largest and 2*num > largest:
                return -1

        return largestIndex


solution = Solution()
print(solution.dominantIndex([1]))