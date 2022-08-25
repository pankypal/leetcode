class Solution(object):
    def decodeString(self, s):
        stack = []

        current_str = ""
        current_count = 0

        for c in s:
            if c.isdigit():
                current_count = current_count * 10 + int(c)
            elif c == "[":
                stack.append((current_count, current_str))
                current_count = 0
                current_str = ""
            elif c == "]":
                prev_count, prev_str = stack.pop()
                current_str = prev_str + prev_count * current_str
            else: 
                current_str += c

        return current_str

solution = Solution()
print(solution.decodeString("3[a2[c]]"))