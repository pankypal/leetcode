class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = list(heights)
        expected.sort()

        result = 0
        for i in range(0,len(heights)):
            if expected[i] != heights[i]:
                result += 1
        
        return result



solution = Solution()
print(solution.heightChecker([1,1,4,2,1,3]))