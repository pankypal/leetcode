class Solution(object):
    def countingSort(self, nums, exp):
        counts = [0] * 10

        for num in nums:
            index = (num // exp) % 10
            counts[index] += 1

        for i in range(1, 10):
            counts[i] += counts[i-1]

        output = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            index = (nums[i] // exp) % 10
            output[counts[index]-1] = nums[i]
            counts[index] -= 1

        for i in range(len(nums)):
            nums[i] = output[i]


    def radix_sort(self, nums):
        if not nums:
            return nums

        largest = max(nums)

        exp = 1
        while largest / exp >= 1:
            self.countingSort(nums, exp)
            exp *= 10

        return nums

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        
        nums = self.radix_sort(nums)

        gap = 0
        for i in range(1, len(nums)):
            gap = max(gap, nums[i]-nums[i-1])

        return gap
        

solution = Solution()
print(solution.maximumGap([3,6,9,1]))