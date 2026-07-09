# 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, 
# and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return true if n new flowers can be planted
# in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return True

        end = len(flowerbed)
        for i, el in enumerate(flowerbed):
            if n <= 0:
                break

            if el == 0 and (i == 0 or flowerbed[i - 1] != 1) and ((i == end - 1) or flowerbed[i + 1] != 1):
                n -= 1
                flowerbed[i] = 1

        if n <= 0:
            return True
        else:
            return False
        

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1,0,0], 2))