import sortedcontainers

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        pairs = []

        for b in buildings:
            pairs.append((b[0], -b[2]))
            pairs.append((b[1], b[2]))

        pairs.sort()

        ans = []
        heights = sortedcontainers.SortedList([0])

        currmaxH = 0

        for point in pairs:
            if point[1] < 0:
                heights.add(-point[1])
            else:
                heights.remove(point[1])

            if currmaxH != heights[-1]:
                currmaxH = heights[-1]
                ans.append([point[0], currmaxH])

        return ans

        

solution = Solution()
print(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))