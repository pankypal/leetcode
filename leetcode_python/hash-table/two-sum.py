class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = dict()
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in data:
                return [data[target - num], i]
            
            data[num] = i
        
        return
        

solution = Solution()
print(solution.twoSum([1,2,4], 6))