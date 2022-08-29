class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0

        if x == 1:
            return 1

        if n == 0:
            return 1

        isNegative = (x < 0) and (n%2!=0)
        map = {}

        isDivision = n < 0
        res = self._myPow(abs(x), abs(n), map)

        res = -1*res if isNegative else res
        if isDivision:
            return 1/res
        else:
            return res


    def _myPow(self, x, n, map):
        if n in map:
            return map[n]

        if n == 1:
            return x

        y = self._myPow(x, n//2, map)
        res = y *y
        if n % 2 != 0:
            res *= x
        map[n] = res

        return res

solution = Solution()
print(solution.myPow(-4, -3))