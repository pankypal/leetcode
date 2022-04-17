class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        len_hay = len(haystack)
        len_needle = len(needle)

        if not needle:
            return 0

        if len_hay < len_needle:
            return -1

        for i in range(len_hay-len_needle+1):
            j = 0
            while j < len_needle and haystack[i+j] == needle[j]:
                j += 1

            if j == len_needle:
                return i

        return -1
        

solution = Solution()
print(solution.strStr("hello", "ll"))