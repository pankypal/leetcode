from math import ceil
from pickletools import markobject


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        startRow = 0
        endRow = len(matrix)
        startCol = 0
        endCol = len(matrix[0])
        result = []
        
        while startRow < endRow and startCol < endCol:

            i = startCol
            while i < endCol:
                result.append(matrix[startRow][i])
                i += 1
            
            startRow += 1

            i = startRow
            while i < endRow:
                result.append(matrix[i][endCol-1])
                i += 1

            endCol -= 1

            if startRow >= endRow or startCol >= endCol:
                break

            i = endCol - 1
            while i >= startCol:
                result.append(matrix[endRow-1][i])
                i -= 1

            endRow -= 1

            i = endRow - 1
            while i >= startRow:
                result.append(matrix[i][startCol])
                i -= 1

            startCol += 1

        return result


solution = Solution()
print(solution.spiralOrder( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))