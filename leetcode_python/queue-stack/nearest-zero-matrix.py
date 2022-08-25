import sys
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat:
            return mat

        nrows = len(mat)
        ncols = len(mat[0])

        dp = [[sys.maxsize for _ in range(ncols)] for _ in range(nrows)]

        for i in range(nrows):
            for j in range(ncols):
                if mat[i][j] == 0:
                    dp[i][j] = 0

                else:
                    if i > 0:
                        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j])
                    if j > 0:
                        dp[i][j] = min(dp[i][j-1] + 1, dp[i][j])

        
        for i in range(nrows-1, -1, -1):
            for j in range(ncols -1, -1, -1):
                if i < nrows - 1:
                    dp[i][j] = min(dp[i+1][j] + 1, dp[i][j])
                if j < ncols - 1:
                    dp[i][j] = min(dp[i][j+1] + 1, dp[i][j])

        return dp



solution = Solution()
print(solution.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]))