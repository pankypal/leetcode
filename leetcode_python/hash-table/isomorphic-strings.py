class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = dict()
        values = set()

        for i in range(len(s)):
            ch = s[i]
            if ch in map and map[ch] != t[i]:
                return False
            
            if ch not in map and t[i] in values:
                return False

            map[ch] = t[i]
            values.add(t[i])

        return True

    def isIsomorphic1(self, s, t):
        return self.helper(s) == self.helper(t)

    def helper(self, s):
        map = dict()
        newString = []

        for i in range(len(s)):
            ch = s[i]
            if ch not in map:
                map[ch] = i
            
            newString.append(str(map[ch]))

        return " ".join(newString)


solution = Solution()
print(solution.isIsomorphic("title", "paper"))
print(solution.isIsomorphic1("title", "paper"))