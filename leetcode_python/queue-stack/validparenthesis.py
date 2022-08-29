
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    return False
                topVal = stack.pop()
                if (c == ")" and topVal != "(") or (c == "}" and topVal != "{") or (c == "]" and topVal != "["):
                    return False

        
        return True if len(stack) == 0 else False


solution = Solution()
print(solution.isValid("{[()]}"))