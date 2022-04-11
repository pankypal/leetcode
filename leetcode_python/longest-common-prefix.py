class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            temp = strs[i]

            j = 0
            while j < len(prefix) and j < len(temp) and prefix[j] == temp[j]:
                j += 1

            prefix = prefix[:j]
            if not prefix:
                return ""

        return prefix

    def lcp_r(self, strs, start, end):
        if start == end:
            return strs[start]

        mid = (start + end) // 2
        lcpleft = self.lcp_r(strs, start, mid)
        lcpRight = self.lcp_r(strs, mid+1, end)
        return self.commonPrefix(lcpleft, lcpRight)

    def commonPrefix(self, left, right):
        i = 0
        while i < len(left) and i < len(right) and left[i] == right[i]:
            i += 1

        return left[:i]

    def lcp(self, strs):
        if (len(strs) == 0):
            return ""

        return self.lcp_r(strs, 0, len(strs)-1)

        

solution = Solution()
print(solution.longestCommonPrefix(["leets", "leetcode", "leet", "leeds"]))
print(solution.lcp(["leets", "leetcode", "leet", "leeds"]))