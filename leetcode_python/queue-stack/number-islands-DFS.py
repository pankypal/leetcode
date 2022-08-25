class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    count += 1
                    self.searchDFS(grid, i, j, visited)

        return count

    def searchDFS(self, grid, i, j, visited):
        visited[i][j] = True

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for d in directions:
            r,c = i + d[0], j + d[1]
            if self.isValid(grid, r,c) and grid[r][c] == "1" and visited[r][c] == False:
                self.searchDFS(grid, r, c, visited)

    def isValid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        
        return True

solution = Solution()
print(solution.numIslands([
   ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))