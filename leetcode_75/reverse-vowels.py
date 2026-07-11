# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        inp = list(s)

        while start < end:
            if inp[start] in vowels and inp[end] in vowels:
                inp[start], inp[end] = inp[end], inp[start]
                start += 1
                end -= 1
            elif inp[start] not in vowels:
                start += 1
            elif inp[end] not in vowels:
                end -= 1

        return "".join(inp)

    
    def isVowel_1(self, c):
        return c in "aeiou"

    def reverseVowels1(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        
        # Two-pointer approach to swap vowels
        while left < right:
            
            # Move left pointer until a vowel is found
            while left < right and not self.isVowel_1(s[left]):
                left += 1

            # Move right pointer until a vowel is found
            while left < right and not self.isVowel_1(s[right]):
                right -= 1

            # Swap the vowels
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return "".join(s)



sol = Solution()
print(sol.reverseVowels("leetcode"))
