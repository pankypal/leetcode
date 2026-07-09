# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" 
# if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        len_gcd = self.gcd(len(str1), len(str2))

        return str1[:len_gcd]
    
    def gcd(self, n1, n2):
        if n2 == 0:
            return n1
        
        return self.gcd(n2, n1 % n2)
    

    def gcd_1(self, str1, str2):

        # If str1 length is less than
        # that of str2 then recur
        # with gcd(str2, str1)
        if len(str1) < len(str2):
            return self.gcd_1(str2, str1)
        
        # If str1 is not the
        # concatenation of str2
        elif not str1.startswith(str2):
            return ""
        elif len(str2) == 0:
            
            # GCD string is found
            return str1
        else:
            
            # Cut off the common prefix
            # part of str1 & then recur
            return self.gcd_1(str1[len(str2):], str2)

    # Function to find GCD of array of
    # strings
    def findGCD(self, arr, n):
        result = arr[0]

        for i in range(1, n):
            result = self.gcd_1(result, arr[i])
        
        # Return the GCD of strings
        return result
        
        

solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))
print(solution.gcdOfStrings("ABABAB", "ABAB"))
print(solution.gcdOfStrings("AAAAAB", "AAA"))

strs = ["GFGGFG", "GFGGFG", "GFGGFGGFGGFG"]
print(solution.findGCD(strs, 3))