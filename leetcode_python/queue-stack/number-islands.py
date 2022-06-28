from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        check = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and check[i][j] == False:
                    count += 1
                    self.serachBfs(grid, i, j, check)

        return count

    def serachBfs(self, grid, i, j, check):
        q = deque()
        q.append((i, j))
        check[i][j] = True

        while q:
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            i, j = q.popleft()

            for d in directions:
                r, c = i + d[0], j + d[1]
                if self.isValid(grid, r, c) and grid[r][c] == "1" and check[r][c] == False:
                    q.append((r,c))
                    check[r][c] = True

    def isValid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

solution = Solution()
print(solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))