class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        f0 = 0
        f1 = 1
        res = 0
        for _ in range(2, n+1):
            res = f0 + f1
            f0 = f1
            f1 = res

        return res

solution = Solution()
print(solution.fib(7))