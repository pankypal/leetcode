class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        word = ''
        for i in range(len(s)):
            if s[i] == ' ':
                res += word[::-1]
                res += ' '
                word = ''
            else:
                word += s[i]

        res += word[::-1]

        return res


        
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))