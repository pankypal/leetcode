class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0

        half = 2**(n-2)

        if k <= half:
            return self.kthGrammar(n-1, k)
        else:
            res = self.kthGrammar(n-1, k-half)
            return 1 if res == 0 else 0

        
solution = Solution()
print(solution.kthGrammar(30, 434991989))