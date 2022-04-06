class Solution(object):
    def duplicateZeros(self, arr):
        count_zeros = arr.count(0)

        size = len(arr)
        i = size - 1
        j = size + count_zeros - 1

        while j >= 0:
            if arr[i] == 0:
                if j < size:
                    arr[j] = 0
                j -= 1
                if j < size:
                    arr[j] = 0
                j -= 1
                i -= 1
            else:
                if j < size:
                    arr[j] = arr[i]
                j -= 1
                i -= 1

        return arr

    
solution = Solution()
print(solution.duplicateZeros([1,2]))