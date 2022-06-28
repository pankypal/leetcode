from collections import deque
from dis import dis


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        visited = set('0000')
        dead_set = set(deadends)
        queue = deque()

        queue.append(('0000', 0))

        while queue:
            string, distance = queue.popleft()

            if string == target:
                return distance

            if string in dead_set:
                continue

            for i in range(4):
                val = int(string[i])

                for j in [-1, 1]:
                    new_val = (val + j) % 10
                    new_string = string[:i] + str(new_val) + string[i+1:]
                    if new_string not in visited and new_string not in dead_set:
                        queue.append((new_string, distance+1))
                        visited.add(new_string)

        return -1
        
solution = Solution()
print(solution.openLock( ["0000"], "8888"))