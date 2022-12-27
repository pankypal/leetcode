class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return nums

        steps = len(nums[0])
        results = []
        output = [i for i in range(len(nums))]

        for step in range(1, steps+1):
            counts = [0] * 10

            for num in nums:
                index = int(num[-step])
                counts[index] += 1

            for i in range(1, 10):
                counts[i] += counts[i-1]

            nxt = [0] * len(nums)
            for i in output[::-1]:
                index = int(nums[i][-step])
                nxt[counts[index]-1] = i
                counts[index] -= 1

            output = nxt
            results.append(output)

        return [results[trim - 1][rank - 1] for rank, trim in queries]


solution = Solution()
print(solution.smallestTrimmedNumbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]))