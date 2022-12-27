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

    def selectionSort(self, nums):
        if not nums:
            return nums

        for i in range(len(nums)):
            maxIndex = 0
            endIndex = len(nums) - i
            for j in range(1, endIndex):
                if nums[j] > nums[maxIndex]:
                    maxIndex = j
            
            nums[maxIndex], nums[endIndex-1] = nums[endIndex-1], nums[maxIndex]

        return nums

    def bubbleSort(self, nums):
        if not nums:
            return nums
        
        didSwap = True

        while didSwap:
            didSwap = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    didSwap = True
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                i += 1

        return nums

    def heapSort(self, nums):
        def heapify(index, heap_size):
            left = 2*index + 1
            right = 2*index + 2

            largest = index
            if left <= heap_size and nums[left] > nums[largest]:
                largest = left
            if right <= heap_size and nums[right] > nums[largest]:
                largest = right

            if largest != index:
                nums[index], nums[largest] = nums[largest], nums[index]
                heapify(largest, heap_size)

        for i in range(len(nums) // 2 -1, -1, -1):
            heapify(i, len(nums)-1)

        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(0, i-1)

        return nums

    def countSort(self, nums):
        if not nums:
            return nums

        largest = max(nums)
        counts = [0] * (largest+1)

        for num in nums:
            counts[num] += 1

        for i in range(1, largest+1):
            counts[i] += counts[i-1]

        output = [0]*len(nums)
        for num in nums:
            output[counts[num]-1] = num
            counts[num] -= 1

        return output





solution = Solution()
print(solution.sortArray([5,1,1,2,0,0]))
print(solution.quickSort([5,1,1,2,0,0]))
print(solution.insertionSort([5,1,1,2,0,0]))
print(solution.selectionSort([5,1,1,2,0,0]))
print(solution.bubbleSort([5,1,1,2,0,0]))
print(solution.heapSort([5,1,1,2,0,0]))
print(solution.countSort([5,4,5,5,1,1,3]))