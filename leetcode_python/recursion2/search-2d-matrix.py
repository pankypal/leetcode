class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        if m == 0 or n == 0:
            return False

        i = 0
        j = n -1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False

        

sol = Solution()
print(sol.searchMatrix([
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]], 18))