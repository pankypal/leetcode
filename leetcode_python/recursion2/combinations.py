class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            raise Exception("invalid input")


        res = []
        self.generateCombos(1, n, k, [], res)
        return res

    def generateCombos(self, start, n, k, prefix, res):
        if k == 0:
            res.append(prefix)
            return

        for i in range (start, n+1):
            self.generateCombos(i+1, n, k-1, prefix+[i], res)
        

solution = Solution()
print(solution.combine(3, 2))