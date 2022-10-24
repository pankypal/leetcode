class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        if len(heights) == 1:
            return heights[0]

        st = [0]

        maxArea = 0

        for i in range(1, len(heights)):
            curr = heights[i]

            while st and curr < heights[st[-1]]:
                topStack = st.pop()

                if not st:
                    area =  heights[topStack] * i
                else:
                    area = heights[topStack] * (i - st[-1] - 1)
                maxArea = max(maxArea, area)

            st.append(i)

        while st:
            curr = st.pop()

            if not st:
                area = heights[curr] * len(heights)
            else:
                area = heights[curr] * (len(heights) - st[-1] - 1)
            maxArea = max(maxArea, area)

        return maxArea

        

solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))
print(solution.largestRectangleArea([2,4]))
print(solution.largestRectangleArea([2,2]))
print(solution.largestRectangleArea([2,1,2]))