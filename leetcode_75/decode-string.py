# 394. Decode String

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        nums = []
        strings = []

        currentNum = 0
        currentStr = ""

        for ch in s:
            if ch.isdigit():
                currentNum = currentNum * 10 + int(ch)
            elif ch == '[':
                nums.append(currentNum)
                strings.append(currentStr)
                currentStr = ""
                currentNum = 0
            elif ch == ']':
                prev = strings.pop()
                count = nums.pop()
                currentStr = prev + currentStr * count
            else:
                currentStr += ch

        return currentStr

sol = Solution()
#print(sol.decodeString("2[abc]3[cd]ef"))
print(sol.decodeString("3[a2[c]]"))