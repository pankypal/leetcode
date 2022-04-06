from typing import Set


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        doubles = set()
        for num in arr:
            if num*2 in doubles:
                return True

            if num %2 == 0 and num/2 in doubles:
                return True
            
            doubles.add(num)

        return False

solution = Solution()
print('Result:', solution.checkIfExist([3, 1, 7, 11]))