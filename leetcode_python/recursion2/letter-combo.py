
class Solution(object):
    digitsMap = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []

        if not digits:
            return res

        self.combos(digits, 0, "", res)

        return res

    def combos(self, digits, curr, prefix, res):
        if curr == len(digits):
            res.append(prefix)
            return

        letter = digits[curr]

        for ch in Solution.digitsMap[letter]:
            self.combos(digits, curr+1, prefix+ch, res)
        
                

solution = Solution()
print(solution.letterCombinations("7"))