from posixpath import split

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = ''

        for word in reversed(words):
            if res:
                res += " "
            res += word

        return res



solution = Solution()
print(solution.reverseWords(" a   good example  "))