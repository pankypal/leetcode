class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data = set()

        for num in nums:
            if num in data:
                return True

            data.add(num)

        return False

solution = Solution()
print(solution.containsDuplicate([1,3,4,2]))