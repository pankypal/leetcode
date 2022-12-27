import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return nums

        pivot = random.choice(nums)

        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]

        len_left, len_mid = len(left), len(mid)

        if k <= len_left:
            return self.findKthLargest(left, k)
        elif k > len_left + len_mid:
            return self.findKthLargest(right, k - len_left - len_mid)
        else:
            return mid[0]

    def findKthLargest1(self, nums, k):
        return self.qsort(nums, 0, len(nums)-1, k)

    def qsort(self, nums, low, high, k):
        randomindex = random.randint(low, high)
        nums[randomindex], nums[high] = nums[high], nums[randomindex]
        pivot = high

        i = low
        for j in range(low, high):
            if nums[j] <= nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]

        right = high - i + 1

        if k == right:
            return nums[i]
        
        if right > k:
            return self.qsort(nums, i+1, high, k)

        return self.qsort(nums, low, i-1, k-right)


solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4], 2))
print(solution.findKthLargest1([3,2,1,5,6,4], 2))