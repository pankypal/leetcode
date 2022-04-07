class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 1
        for num in reversed(digits):
            sum = num + carry
            carry = sum // 10
            result.append(sum % 10)

        if carry != 0:
            result.append(carry)

        return result[::-1]



solution = Solution()
print(solution.plusOne([9]))