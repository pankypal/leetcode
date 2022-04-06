

class Solution(object):
    def findNumbers(self, nums):
        count_event = 0

        for num in nums:
            if (self.countNumberDigits(num) % 2 == 0):
                count_event += 1
        
        return count_event

    def countNumberDigits(self, num):
        count = 0
        while num > 0:
            num = num // 10
            count += 1

        return count

solution = Solution()
print(solution.findNumbers([555,901,482,1771]))