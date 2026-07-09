class Solution(object):
    def isHappy(self, n):
        store = set()

        return self.helper(n, store)

    def helper(self, n, store):
        newN = 0
        while n:
            digit = n % 10
            newN += digit * digit
            n = n // 10

        if newN == 1:
            return True
        else:
            if newN in store:
                return False

            store.add(newN)
            return self.helper(newN, store)



solution = Solution()
print(solution.isHappy(116))