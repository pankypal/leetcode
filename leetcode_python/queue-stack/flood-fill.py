from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if not image:
            return image

        if not self.isValid(image, sr, sc):
            return image

        q = deque()
        currColor = image[sr][sc]

        if color == currColor:
            return image

        q.append((sr, sc))
        image[sr][sc] = color

        while q:
            curr_i, curr_j = q.popleft()

            directions = [(1,0), (0,1), (-1, 0), (0, -1)]
            for d in directions:
                i = curr_i + d[0]
                j = curr_j + d[1]

                if self.isValid(image, i, j) and image[i][j] == currColor:
                    q.append((i, j))
                    image[i][j] = color

        return image


    def isValid(self, image, r, c):
        m, n = len(image), len(image[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        
        return True


solution = Solution()
print(solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))