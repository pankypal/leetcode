# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, 
# append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1:
            return word2
        
        if not word2:
            return word1

        i = j = 0
        res = ""

        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]

            i += 1
            j += 1

        while i < len(word1):
            res += word1[i]
            i += 1

        while j < len(word2):
            res += word2[j]
            j += 1

        return res


solution = Solution()
print(solution.mergeAlternately("abcd", "pqrs"))