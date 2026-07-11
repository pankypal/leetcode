# 151. Reverse Words in a String

# Input: s = "the sky is blue"
# Output: "blue is sky the"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        words = []
        i = 0

        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1

            start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            
            end = i

            if start != end:
                words.append(s[start:end])

        return " ".join(words[::-1])


        
sol = Solution()
print(">", sol.reverseWords("    the sky is   blue   "), "<", sep="")
print(">", sol.reverseWords("  "), "<", sep="")