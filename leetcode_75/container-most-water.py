# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water. 
# Return the maximum amount of water a container can store.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0
        
        i = 0
        j = len(height) - 1

        area = 0

        while i < j:
            area = max(area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area

        

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))