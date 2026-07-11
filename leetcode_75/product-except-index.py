# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [0] * len(nums)
        ans = [0] * len(nums)

        if not nums:
            return temp
        
        mult = 1
        for i in range(len(nums)-1, -1, -1):
            temp[i] = mult
            mult *= nums[i]

        mult = 1
        for i, el in enumerate(nums):
            ans[i] = temp[i] * mult
            mult *= el

        return ans

        
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,1,0,-3,3]))