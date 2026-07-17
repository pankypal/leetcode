# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if not arr:
            return True
        
        freq = dict()
        freq_set = set()

        for el in arr:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1

        for val in freq:
            if freq[val] in freq_set:
                return False
            
            freq_set.add(freq[val])

        return True

        

sol = Solution()
print(sol.uniqueOccurrences([1,2]))