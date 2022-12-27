class Solution(object):
    def minimumAbsDifference(self, arr):
        if len(arr) < 2:
            return arr

        arr.sort()

        min_diff = float("+inf")

        for i in range(1, len(arr)):
            min_diff = min(arr[i] - arr[i-1], min_diff)

        output = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                output.append([arr[i-1], arr[i]])

        return output


solution = Solution()
print(solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))