from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        nrooms = len(rooms)
        visited = [False] * nrooms 
        q = deque()

        q.append(rooms[0])
        visited[0] = True

        while q:
            curr = q.popleft()
            for n in curr:
                if not visited[n]:
                    q.append(rooms[n])
                    visited[n] = True

        for el in visited:
            if el == False:
                return False

        return True


solution = Solution()
print(solution.canVisitAllRooms([[1],[2],[3],[]]))