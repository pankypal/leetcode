# 1657. Determine if Two Strings Are Close

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


class Solution(object):

    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        len1 = len(word1)
        len2 = len(word2)

        if len1 != len2:
            return False
        
        set1 = set()
        set2 = set()
        for i in range(len1):
            set1.add(word1[i])
            set2.add(word2[i])

        if set1 != set2:
            return False
        
        freq1 = {}
        freq2 = {}
        for el in word1:
            if el in freq1:
                freq1[el] += 1
            else:
                freq1[el] = 1

        for el in word2:
            if el in freq2:
                freq2[el] += 1
            else:
                freq2[el] = 1
        
        return sorted(freq1.values()) == sorted(freq2.values())



sol = Solution()
# print(sol.closeStrings("cabbba", "aabbss"))
print(sol.closeStrings("cabbba", "abbccc"))
