class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)

        if size < 1:
            return

        k =  k % size
        self.rev(nums, 0, size-1)
        self.rev(nums, 0, k-1)
        self.rev(nums, k, size-1)

    def rev(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end],nums[start]
            start += 1
            end -=  1
        


solution = Solution()
nums = [1,2,3,4,5,6,7]
solution.rotate(nums, 3)
print(nums)