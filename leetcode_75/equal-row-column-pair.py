# 2352. Equal Row and Column Pairs

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dict1 = {}

        for row in grid:
            key = tuple(row)
            if key in dict1:
                dict1[key] += 1
            else:
                dict1[key] = 1

        count = 0
        nrows = len(grid)
        for j in range(nrows):
            col_key = tuple(grid[i][j] for i in range(nrows))
            if col_key in dict1:
                count += dict1[col_key]

        return count
        


sol = Solution()
print(sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))