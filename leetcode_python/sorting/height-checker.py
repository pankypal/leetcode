class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        heightFreq = [0] * 101

        for height in heights:
            heightFreq[height] += 1

        j = 0
        result = 0
        for i in range(len(heights)):
            while heightFreq[j] == 0:
                j += 1

            if j != heights[i]:
                result += 1

            heightFreq[j] -= 1

        return result

        

solution = Solution()
print(solution.heightChecker([1,1,4,2,1,3]))