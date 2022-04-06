
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        result = []

        for num in nums:
            index = abs(num)
            if nums[index-1] > 0:
                nums[index-1] *= -1
        
        for i in range(0, size):
            if nums[i] > 0:
                result.append(i+1)

        return result


solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))