class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1, end+1]

            if sum < target:
                start += 1
            else:
                end -= 1

        return [-1, -1]
        

solution = Solution()
print(solution.twoSum([-1,0], -1))