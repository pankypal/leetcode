class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        size = len(arr)
        largest = -1
        result = [largest] * size

        index = size - 1
        while index >= 0:
            result[index] = largest
            largest = max(arr[index], largest)
            index -= 1

        return result

solution = Solution ()
print(solution.replaceElements([30]))