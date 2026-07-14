# 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = set('aeiou')
        maxCount = 0
        currcount = 0

        i = j = 0
        while j < k:
            if s[j] in vowels:
                currcount += 1
            j += 1

        maxCount = currcount

        for j in range(k, len(s)):
            if s[i] in vowels:
                currcount -= 1

            if s[j] in vowels:
                currcount += 1

            maxCount = max(currcount, maxCount)

            i += 1

        return maxCount
        

sol = Solution()
print(sol.maxVowels("abciiidef", 3))