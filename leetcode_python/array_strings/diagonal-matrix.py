from unittest import result


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        nrows = len(mat)
        ncols = len(mat[0])
        dir = 'up'
        result = []

        for col in range(ncols):
            diag = []
            i = 0
            j = col

            while i < nrows and j >= 0:
                diag.append(mat[i][j])
                i += 1
                j -= 1

            if dir is 'up':
                diag.reverse()
            
            result += diag
            dir = 'down' if dir == 'up' else 'up'

        for row in range(1, nrows):
            diag = []
            i = row
            j = ncols-1

            while i < nrows and j >= 0:
                diag.append(mat[i][j])
                i += 1
                j -= 1

            if dir is 'up':
                diag.reverse()
            
            result += diag
            dir = 'down' if dir == 'up' else 'up'
        
        return result

solution = Solution()
print(solution.findDiagonalOrder([[1,2,3],[4,5,6]]))