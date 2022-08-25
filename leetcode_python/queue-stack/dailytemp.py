class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)

        stack = []
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append(index)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    topIndex = stack[-1]
                    answer[topIndex] = index - topIndex
                    stack.pop()

                stack.append(index)
                

        return answer



solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))