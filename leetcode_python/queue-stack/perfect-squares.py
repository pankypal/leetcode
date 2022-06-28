from collections import deque


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return n

        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1

        queue = deque()
        queue.append(n)

        level = 0

        while queue:
            tmp = deque()
            level += 1

            for el in queue:
                for square in squares:
                    if el == square:
                        return level
                    
                    if el < square:
                        break

                    tmp.append(el-square)

            queue = tmp

        return level

        
solution = Solution()
print(solution.numSquares(13))