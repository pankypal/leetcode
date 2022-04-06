class Solution(object):
    def sortedSquares(self, nums):
        ans = []
        start = 0
        end = len(nums) - 1

        while start <= end:
            if abs(nums[start]) < abs(nums[end]):
                ans.append(nums[end]**2)
                end -= 1
            else:
                ans.append(nums[start]**2)
                start += 1
        
        return ans[::-1]

     
solution = Solution()
print(solution.sortedSquares([-7,-3,2,3,11]))