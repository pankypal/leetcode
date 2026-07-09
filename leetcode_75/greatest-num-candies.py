# 1431. Kids With the Greatest Number of Candies
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
#
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
#
# Note that multiple kids can have the greatest number of candies.


class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        res = [False] * len(candies)
        if not candies:
            return None
        
        max_val = self.getMax(candies)

        for i, el in enumerate(candies):
            if el + extraCandies >= max_val:
                res[i] = True
            else:
                res[i] = False

        return res



    def getMax(self, arr):
        maxVal = arr[0]

        for i in range(1, len(arr)):
            maxVal = max(arr[i], maxVal)

        return maxVal

solution = Solution()
print(solution.kidsWithCandies([4,2,1,1,2], 1))