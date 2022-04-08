class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)

        str_a = a[::-1]
        str_b = b[::-1]

        result = ""
        carry = 0
        i = j = 0
        while i < len_a and j < len_b:
            sum = (int(str_a[i]) + int(str_b[j]) + carry) % 2
            carry = (int(str_a[i]) + int(str_b[j]) + carry) // 2
            result += str(sum)
            i += 1
            j += 1

        while i < len_a:
            sum = (int(str_a[i]) + carry) % 2
            carry = (int(str_a[i]) + carry) // 2
            result += str(sum)
            i += 1

        while j < len_b:
            sum = (int(str_b[j]) + carry) % 2
            carry = (int(str_b[j]) + carry) // 2
            result += str(sum)
            j += 1

        if carry == 1:
            result += str(1)

        return result[::-1]



solution = Solution()
print(solution.addBinary("100", "110010"))