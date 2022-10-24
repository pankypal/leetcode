class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        mid = int(len(nums)/2)
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        res = []

        m = len(left)
        n = len(right)
        i = j = 0
        while i < m and j < n:
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])

        return res

    def quickSort(self, nums):
        self.qSort(nums, 0, len(nums)-1)
        return nums

    def qSort(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.qSort(nums, low, pivot-1)
            self.qSort(nums, pivot+1, high)


    def partition(self, nums, low, high):
        i = low
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[high] = nums[high], nums[i]

        return i

    def insertionSort(self, nums):
        if not nums:
            return nums

        n = len(nums)
        for i in range(1, n):
            curr = nums[i]
            j = i -1
            while j >= 0 and nums[j] > curr:
                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = curr
        
        return nums

            



solution = Solution()
print(solution.sortArray([5,1,1,2,0,0]))
print(solution.quickSort([5,1,1,2,0,0]))
print(solution.insertionSort([5,1,1,2,0,0]))