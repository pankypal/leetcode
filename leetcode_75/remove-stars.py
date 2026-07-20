# 2390. Removing Stars From a String

# You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s. 
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        st = []

        for ch in s:
            if ch == '*':
                st.pop()
            else:
                st.append(ch)

        return "".join(st)


sol = Solution()
print(sol.removeStars("leet**cod*e"))