class Solution(object):
    def generateParens(self, num):
        self.res = []
        self.generate(0, 0, "", num)

        return self.res

    def generate(self, openN, closeN, str, num):
        if openN == closeN == num:
            self.res.append(str)
            return

        if openN < num:
            self.generate(openN+1, closeN, str+"(", num)

        if closeN < openN:
            self.generate(openN, closeN+1, str+")", num)



solution = Solution()
print(solution.generateParens(3))